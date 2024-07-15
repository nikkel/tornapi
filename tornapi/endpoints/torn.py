from typing import Any, Dict, Optional, List, Union


class TornEndpoint:
    def __init__(self, api: Any):
        self.api = api

    def _get_torn_data(self, selection: str, _id: Optional[Union[int, str]] = None) -> Dict[str, Any]:
        endpoint = f"torn{f'/{_id}' if _id else ''}"
        params = {'selections': selection}
        return self.api.make_request(endpoint, params)

    def bank(self) -> Dict[str, Any]:
        return self._get_torn_data("bank")

    def cards(self) -> Dict[str, Any]:
        return self._get_torn_data("cards")

    def chainreport(self, chain_id: int) -> Dict[str, Any]:
        return self._get_torn_data("chainreport", chain_id)

    def cityshops(self) -> Dict[str, Any]:
        return self._get_torn_data("cityshops")

    def companies(self, company_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_torn_data("companies", company_id)

    def competition(self) -> Dict[str, Any]:
        return self._get_torn_data("competition")

    def dirtybombs(self) -> Dict[str, Any]:
        return self._get_torn_data("dirtybombs")

    def education(self, education_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_torn_data("education", education_id)

    def factiontree(self) -> Dict[str, Any]:
        return self._get_torn_data("factiontree")

    def getCards(self) -> Dict[str, Any]:
        return self._get_torn_data("getCards")

    def getDirtyBombs(self) -> Dict[str, Any]:
        return self._get_torn_data("getDirtyBombs")

    def gyms(self, gym_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_torn_data("gyms", gym_id)

    def honors(self, honor_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_torn_data("honors", honor_id)

    def itemdetails(self, unique_id: int) -> Dict[str, Any]:
        return self._get_torn_data("itemdetails", unique_id)

    def items(self, item_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_torn_data("items", item_id)

    def itemstats(self) -> Dict[str, Any]:
        return self._get_torn_data("itemstats")

    def logcategories(self) -> Dict[str, Any]:
        return self._get_torn_data("logcategories")

    def logtypes(self) -> Dict[str, Any]:
        return self._get_torn_data("logtypes")

    def lookup(self) -> Dict[str, Any]:
        return self._get_torn_data("lookup")

    def medals(self, medal_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_torn_data("medals", medal_id)

    def organisedcrimes(self, oc_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_torn_data("organisedcrimes", oc_id)

    def pawnshop(self) -> Dict[str, Any]:
        return self._get_torn_data("pawnshop")

    def pokertables(self) -> Dict[str, Any]:
        return self._get_torn_data("pokertables")

    def properties(self, property_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_torn_data("properties", property_id)

    def rackets(self) -> Dict[str, Any]:
        return self._get_torn_data("rackets")

    def raidreport(self, raid_id: int) -> Dict[str, Any]:
        return self._get_torn_data("raidreport", raid_id)

    def raids(self) -> Dict[str, Any]:
        return self._get_torn_data("raids")

    def rankedwarreport(self, ranked_war_id: int) -> Dict[str, Any]:
        return self._get_torn_data("rankedwarreport", ranked_war_id)

    def rankedwars(self) -> Dict[str, Any]:
        return self._get_torn_data("rankedwars")

    def rockpaperscissors(self) -> Dict[str, Any]:
        return self._get_torn_data("rockpaperscissors")

    def searchforcash(self) -> Dict[str, Any]:
        return self._get_torn_data("searchforcash")

    def shoplifting(self) -> Dict[str, Any]:
        return self._get_torn_data("shoplifting")

    def stats(self) -> Dict[str, Any]:
        return self._get_torn_data("stats")

    def stocks(self, stock_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_torn_data("stocks", stock_id)

    def territory(self, territories: Optional[Union[str, List[str]]]) -> Dict[str, Any]:
        """
        :param territories: str "AAB" or list of strings ["AAB", "XGA", ...]
        """
        return self._get_torn_data(
            "territory",
            ",".join(territories) if isinstance(territories, list) else territories
        )

    def territorynames(self) -> Dict[str, Any]:
        return self._get_torn_data("territorynames")

    def territorywarreport(self) -> Dict[str, Any]:
        return self._get_torn_data("territorywarreport")

    def territorywars(self) -> Dict[str, Any]:
        return self._get_torn_data("territorywars")

    def timestamp(self) -> Dict[str, Any]:
        return self._get_torn_data("timestamp")
