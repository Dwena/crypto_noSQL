from datetime import datetime


class Utils:
    @staticmethod
    def get_current_time(date_str):
        date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return date_obj.strftime("%m-%d-%Y")

    @staticmethod
    def from_iso_to_timestamp(date_str):
        date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return date_obj.timestamp() * 1000

    @staticmethod
    def get_time_from_timestamp(date_str):
        a = []
        for d in date_str:
            date_obj = datetime.fromtimestamp(d['date'] / 1000)
            a.append({"date": date_obj.strftime('%Y-%m-%d'), "price": d['price']})
        return a
