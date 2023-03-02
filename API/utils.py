from datetime import datetime

class Utils:
    @staticmethod
    def get_current_time(date_str):
        date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return date_obj.strftime("%m-%d-%Y")
