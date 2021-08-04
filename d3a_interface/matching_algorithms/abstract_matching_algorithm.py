from abc import ABC, abstractmethod
from typing import Dict, List

from d3a_interface.dataclasses import BidOfferMatch


class BaseMatchingAlgorithm(ABC):

    @classmethod
    @abstractmethod
    def get_matches_recommendations(
            cls, matching_data: Dict) -> List[BidOfferMatch.serializable_dict]:
        """Calculate and return matches recommendations.

        Args:
            matching_data: {market_uuid: {"offers": [...], "bids": [...], "current_time":"",...}}

        Returns: List[BidOfferMatch.serializable_dict()]
        """