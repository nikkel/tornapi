from typing import Any, Dict, Optional

from tornapi.exceptions import deprecated


class UserEndpoint:
    def __init__(self, api: Any):
        self.api = api

    def _get_user_data(self, selections: str, user_id: Optional[int] = None) -> Dict[str, Any]:
        endpoint = f"user{f'/{user_id}' if user_id else ''}"
        params = {'selections': selections}
        return self.api.make_request(endpoint, params)

    def ammo(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("ammo", user_id)

    def attacks(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("attacks", user_id)

    def attacksfull(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("attacksfull", user_id)

    def bars(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("bars", user_id)

    def basic(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("basic", user_id)

    def battlestats(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("battlestats", user_id)

    def bazaar(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("bazaar", user_id)

    def cooldowns(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("cooldowns", user_id)

    def crimes(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("crimes", user_id)

    def discord(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("discord", user_id)

    def display(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("display", user_id)

    def education(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("education", user_id)

    def equipment(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("equipment", user_id)

    def events(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("events", user_id)

    def gym(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("gym", user_id)

    def hof(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("hof", user_id)

    def honors(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("honors", user_id)

    def icons(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("icons", user_id)

    @deprecated("The inventory selection is no longer available")
    def inventory(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("inventory", user_id)

    def jobpoints(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("jobpoints", user_id)

    def log(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("log", user_id)

    def lookup(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("lookup", user_id)

    def medals(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("medals", user_id)

    def merits(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("merits", user_id)

    def messages(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("messages", user_id)

    def missions(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("missions", user_id)

    def money(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("money", user_id)

    def networth(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("networth", user_id)

    def newevents(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("newevents", user_id)

    def newmessages(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("newmessages", user_id)

    def notifications(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("notifications", user_id)

    def perks(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("perks", user_id)

    def personalstats(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("personalstats", user_id)

    def profile(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("profile", user_id)

    def properties(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("properties", user_id)

    def refills(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("refills", user_id)

    def reports(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("reports", user_id)

    def revives(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("revives", user_id)

    def revivesfull(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("revivesfull", user_id)

    def skills(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("skills", user_id)

    def stocks(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("stocks", user_id)

    def timestamp(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("timestamp", user_id)

    def travel(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("travel", user_id)

    def weaponexp(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("weaponexp", user_id)

    def workstats(self, user_id: Optional[int] = None) -> Dict[str, Any]:
        return self._get_user_data("workstats", user_id)
