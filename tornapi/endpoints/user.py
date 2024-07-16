from typing import Any, Dict, Optional

from tornapi.exceptions import deprecated


class UserEndpoint:
    def __init__(self, api: Any):
        self.api = api

    def _get_user_data(self, selections: str, user_id: Optional[int] = None) -> Dict[str, Any]:
        endpoint = f"user{f'/{user_id}' if user_id else ''}"
        params = {'selections': selections}
        return self.api.make_request(endpoint, params)

    def ammo(self) -> Dict[str, Any]:
        return self._get_user_data("ammo")

    def attacks(self) -> Dict[str, Any]:
        return self._get_user_data("attacks")

    def attacksfull(self) -> Dict[str, Any]:
        return self._get_user_data("attacksfull")

    def bars(self) -> Dict[str, Any]:
        return self._get_user_data("bars")

    def basic(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("basic", user_id)

    def battlestats(self) -> Dict[str, Any]:
        return self._get_user_data("battlestats")

    def bazaar(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("bazaar", user_id)

    def cooldowns(self) -> Dict[str, Any]:
        return self._get_user_data("cooldowns")

    def crimes(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("crimes", user_id)

    def discord(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("discord", user_id)

    def display(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("display", user_id)

    def education(self) -> Dict[str, Any]:
        return self._get_user_data("education")

    def equipment(self) -> Dict[str, Any]:
        return self._get_user_data("equipment")

    def events(self) -> Dict[str, Any]:
        return self._get_user_data("events")

    def gym(self) -> Dict[str, Any]:
        return self._get_user_data("gym")

    def hof(self) -> Dict[str, Any]:
        return self._get_user_data("hof")

    def honors(self) -> Dict[str, Any]:
        return self._get_user_data("honors")

    def icons(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("icons", user_id)

    @deprecated("The inventory selection is no longer available")
    def inventory(self) -> Dict[str, Any]:
        return self._get_user_data("inventory")

    def jobpoints(self) -> Dict[str, Any]:
        return self._get_user_data("jobpoints")

    def log(self) -> Dict[str, Any]:
        return self._get_user_data("log")

    def lookup(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("lookup", user_id)

    def medals(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("medals", user_id)

    def merits(self) -> Dict[str, Any]:
        return self._get_user_data("merits")

    def messages(self) -> Dict[str, Any]:
        return self._get_user_data("messages")

    def missions(self) -> Dict[str, Any]:
        return self._get_user_data("missions")

    def money(self) -> Dict[str, Any]:
        return self._get_user_data("money")

    def networth(self) -> Dict[str, Any]:
        return self._get_user_data("networth")

    def newevents(self) -> Dict[str, Any]:
        return self._get_user_data("newevents")

    def newmessages(self) -> Dict[str, Any]:
        return self._get_user_data("newmessages")

    def notifications(self) -> Dict[str, Any]:
        return self._get_user_data("notifications")

    def perks(self) -> Dict[str, Any]:
        return self._get_user_data("perks")

    def personalstats(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("personalstats", user_id)

    def profile(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("profile", user_id)

    def properties(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("properties", user_id)

    def refills(self) -> Dict[str, Any]:
        return self._get_user_data("refills")

    def reports(self) -> Dict[str, Any]:
        return self._get_user_data("reports")

    def revives(self) -> Dict[str, Any]:
        return self._get_user_data("revives")

    def revivesfull(self) -> Dict[str, Any]:
        return self._get_user_data("revivesfull")

    def skills(self) -> Dict[str, Any]:
        return self._get_user_data("skills")

    def stocks(self) -> Dict[str, Any]:
        return self._get_user_data("stocks")

    def timestamp(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("timestamp", user_id)

    def travel(self) -> Dict[str, Any]:
        return self._get_user_data("travel")

    def weaponexp(self) -> Dict[str, Any]:
        return self._get_user_data("weaponexp")

    def workstats(self) -> Dict[str, Any]:
        return self._get_user_data("workstats")
