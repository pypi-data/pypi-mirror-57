import abc
import datetime
from typing import Optional, List

from dataclasses import dataclass
from enum import Enum

from robotoff.insights._enum import InsightType
from robotoff.insights.normalize import normalize_emb_code
from robotoff.models import ProductInsight
from robotoff.off import get_product, update_emb_codes, \
    add_label_tag, add_category, update_quantity, update_expiration_date, \
    add_brand, add_store
from robotoff.utils import get_logger

logger = get_logger(__name__)


@dataclass
class AnnotationResult:
    status: str
    description: Optional[str] = None


class AnnotationStatus(Enum):
    saved = 1
    updated = 2
    error_missing_product = 3
    error_updated_product = 4
    error_already_annotated = 5
    error_unknown_insight = 6


SAVED_ANNOTATION_RESULT = AnnotationResult(
    status=AnnotationStatus.saved.name,
    description="the annotation was saved")
UPDATED_ANNOTATION_RESULT = AnnotationResult(
    status=AnnotationStatus.updated.name,
    description="the annotation was saved and sent to OFF")
MISSING_PRODUCT_RESULT = AnnotationResult(
    status=AnnotationStatus.error_missing_product.name,
    description="the product could not be found on OFF")
ALREADY_ANNOTATED_RESULT = AnnotationResult(
    status=AnnotationStatus.error_already_annotated.name,
    description="the insight has already been annotated")
UNKNOWN_INSIGHT_RESULT = AnnotationResult(
    status=AnnotationStatus.error_unknown_insight.name,
    description="unknown insight ID")


class InsightAnnotator(metaclass=abc.ABCMeta):
    def annotate(self,
                 insight: ProductInsight,
                 annotation: int,
                 update=True,
                 session_cookie: Optional[str] = None) -> AnnotationResult:
        insight.annotation = annotation
        insight.completed_at = datetime.datetime.utcnow()
        insight.save()

        if annotation == 1 and update:
            return self.update_product(insight, session_cookie=session_cookie)
        
        return SAVED_ANNOTATION_RESULT

    @abc.abstractmethod
    def update_product(self, insight: ProductInsight,
                       session_cookie: Optional[str] = None) -> AnnotationResult:
        pass


class PackagerCodeAnnotator(InsightAnnotator):
    def update_product(self, insight: ProductInsight,
                       session_cookie: Optional[str] = None) -> AnnotationResult:
        emb_code: str = insight.data['text']

        product = get_product(insight.barcode, ['emb_codes'])

        if product is None:
            return MISSING_PRODUCT_RESULT

        emb_codes_str: str = product.get('emb_codes', '')

        emb_codes: List[str] = []
        if emb_codes_str:
            emb_codes = emb_codes_str.split(',')

        if self.already_exists(emb_code, emb_codes):
            return ALREADY_ANNOTATED_RESULT

        emb_codes.append(emb_code)
        update_emb_codes(insight.barcode, emb_codes,
                         server_domain=insight.server_domain,
                         insight_id=insight.id,
                         session_cookie=session_cookie)
        return UPDATED_ANNOTATION_RESULT

    @staticmethod
    def already_exists(new_emb_code: str,
                       emb_codes: List[str]) -> bool:
        emb_codes = [normalize_emb_code(emb_code)
                     for emb_code in emb_codes]

        normalized_emb_code = normalize_emb_code(new_emb_code)

        if normalized_emb_code in emb_codes:
            return True

        return False


class LabelAnnotator(InsightAnnotator):
    def update_product(self, insight: ProductInsight,
                       session_cookie: Optional[str] = None) -> AnnotationResult:
        product = get_product(insight.barcode, ['labels_tags'])

        if product is None:
            return MISSING_PRODUCT_RESULT

        labels_tags: List[str] = product.get('labels_tags') or []

        if insight.value_tag in labels_tags:
            return ALREADY_ANNOTATED_RESULT

        add_label_tag(insight.barcode, insight.value_tag,
                      insight_id=insight.id,
                      server_domain=insight.server_domain,
                      session_cookie=session_cookie)

        return UPDATED_ANNOTATION_RESULT


class CategoryAnnotator(InsightAnnotator):
    def update_product(self, insight: ProductInsight,
                       session_cookie: Optional[str] = None) -> AnnotationResult:
        product = get_product(insight.barcode, ['categories_tags'])

        if product is None:
            return MISSING_PRODUCT_RESULT

        categories_tags: List[str] = product.get('categories_tags') or []

        if insight.value_tag in categories_tags:
            return ALREADY_ANNOTATED_RESULT

        category_tag = insight.value_tag
        add_category(insight.barcode, category_tag,
                     insight_id=insight.id,
                     server_domain=insight.server_domain,
                     session_cookie=session_cookie)

        return UPDATED_ANNOTATION_RESULT


class ProductWeightAnnotator(InsightAnnotator):
    def update_product(self, insight: ProductInsight,
                       session_cookie: Optional[str] = None) -> AnnotationResult:
        product = get_product(insight.barcode, ['quantity'])

        if product is None:
            return MISSING_PRODUCT_RESULT

        quantity: Optional[str] = product.get('quantity') or None

        if quantity is not None:
            return ALREADY_ANNOTATED_RESULT

        weight = insight.data['text']
        update_quantity(insight.barcode, weight,
                        insight_id=insight.id,
                        server_domain=insight.server_domain,
                        session_cookie=session_cookie)

        return UPDATED_ANNOTATION_RESULT


class ExpirationDateAnnotator(InsightAnnotator):
    def update_product(self, insight: ProductInsight,
                       session_cookie: Optional[str] = None) -> AnnotationResult:
        expiration_date: str = insight.data['text']

        product = get_product(insight.barcode, ['expiration_date'])

        if product is None:
            return MISSING_PRODUCT_RESULT

        current_expiration_date = product.get('expiration_date') or None

        if current_expiration_date:
            return ALREADY_ANNOTATED_RESULT

        update_expiration_date(insight.barcode, expiration_date,
                               insight_id=insight.id,
                               server_domain=insight.server_domain,
                               session_cookie=session_cookie)
        return UPDATED_ANNOTATION_RESULT


class BrandAnnotator(InsightAnnotator):
    def update_product(self, insight: ProductInsight,
                       session_cookie: Optional[str] = None) -> AnnotationResult:
        brand: str = insight.data['brand']

        product = get_product(insight.barcode, ['brands_tags'])

        if product is None:
            return MISSING_PRODUCT_RESULT

        brand_tags: List[str] = product.get('brands_tags') or []

        if brand_tags:
            # For now, don't annotate if a brand has already been provided
            return ALREADY_ANNOTATED_RESULT

        add_brand(insight.barcode, brand,
                  insight_id=insight.id,
                  server_domain=insight.server_domain,
                  session_cookie=session_cookie)
        return UPDATED_ANNOTATION_RESULT


class StoreAnnotator(InsightAnnotator):
    def update_product(self, insight: ProductInsight,
                       session_cookie: Optional[str] = None) -> AnnotationResult:
        store: str = insight.data['store']
        store_tag: str = insight.value_tag

        product = get_product(insight.barcode, ['stores_tags'])

        if product is None:
            return MISSING_PRODUCT_RESULT

        stores_tags: List[str] = product.get('stores_tags') or []

        if store_tag in stores_tags:
            return ALREADY_ANNOTATED_RESULT

        add_store(insight.barcode, store,
                  insight_id=insight.id,
                  server_domain=insight.server_domain,
                  session_cookie=session_cookie)
        return UPDATED_ANNOTATION_RESULT


class InsightAnnotatorFactory:
    mapping = {
        InsightType.packager_code.name: PackagerCodeAnnotator(),
        InsightType.label.name: LabelAnnotator(),
        InsightType.category.name: CategoryAnnotator(),
        InsightType.product_weight.name: ProductWeightAnnotator(),
        InsightType.expiration_date.name: ExpirationDateAnnotator(),
        InsightType.brand.name: BrandAnnotator(),
        InsightType.store.name: StoreAnnotator(),
    }

    @classmethod
    def get(cls, identifier: str) -> InsightAnnotator:
        if identifier not in cls.mapping:
            raise ValueError("unknown annotator: {}".format(identifier))

        return cls.mapping[identifier]
