from pymysql.connections import Connection
from src.news_retriever import get_top_news, get_everything
from src.weather_retriever import get_forecast
from src.preference_manager import (
    add_preference, remove_preference, get_user_preferences)
from src.subscription_manager import subscribe, unsubscribe

class CommandExecutor:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def get_top_user(self, arguments : list[str], username: str) -> str:
        if not len(arguments) == 2:
            return 'Invalid parameter count (should be 2)'

        preferences, keywords = arguments

        if preferences == 'my_preferences' and keywords != '':
            return "You can't mix your preferences with keywords"

        if preferences == '':
            preferences = 'None'

        search_in = 'database' if keywords == '' else 'api'

        if preferences == 'my_preferences':
            user_prefs = get_user_preferences(self.conn, username)
            count = len(user_prefs)
            limit = 9 // count
            result = []
            for pref in user_prefs:
                result += get_top_news(self.conn, search_in, keywords, pref)[:limit]

            return '\n'.join(str(news) for news in result)

        if preferences not in {'business', 'entertainment', 'health',
                                'science', 'sports', 'technology', 'None'}:
            return 'Invalid preference'

        return '\n'.join(str(news) for news in get_top_news(self.conn, search_in,
                                                            keywords, preferences))

    def get_everything_user(self, arguments : list[str], username : str = '') -> str:
        if not len(arguments) == 5:
            return 'Invalid parameter count'
        
        keywords, domain, language, sort_by, page_size = arguments
        
        if keywords == '':
            return 'You have to provide keywords'

        if sort_by == '':
            sort_by = 'publishedAt'

        if language == '':
            language = 'en'

        if not page_size.isdigit():
            return 'Page size should be a number'

        if language not in {'ar','de', 'en', 'es', 'fr', 'he', 'it',
                            'nl', 'no', 'pt', 'ru', 'sv', 'ud', 'zh', ''}:
            return 'This language is unsupported'

        if sort_by not in {'publishedAt', 'relevancy', 'popularity'}:
            return 'Sorting method is unsupported'

        if (size := int(page_size)) > 9:
            return 'Max news is 9'

        return '\n'.join(str(news) for news in get_everything(keywords, domain,
                                                              language, sort_by, size))

    def get_weather(self, arguments : list[str], username : str = '') -> str:
        if not len(arguments) == 2:
            return 'Incorrect number of arguments'

        city, country = arguments

        try:
            forecast = get_forecast(city, country)
        except ValueError as v:
            return str(v)

        header = f"{'Date':<12} {'Min Temp (°C)':<15} {'Max Temp (°C)':<15}"
        separator = "=" * len(header)

        rows = "\n".join(f"{date:<12} {min_temp:<15} {max_temp:<15}"
                         for date, min_temp, max_temp in forecast)

        table = "\n".join([header, separator, rows])

        return table

    def add_preference_command(self, arguments : list[str], username : str) -> str:
        if not len(arguments) == 1:
            return 'Incorrect number of arguments'

        (preference, ) = arguments
        return add_preference(self.conn, username, preference)

    def remove_preference_command(self, arguments : list[str], username : str) -> str:
        if not len(arguments) == 1:
            return 'Incorrect number of arguments'

        (preference,) = arguments
        return remove_preference(self.conn, username, preference)

    def subsribe_command(self, arguments : list[str], username) -> str:
        if not len(arguments) == 1:
            return 'Invalid number of arguments'

        (email, ) = arguments

        return subscribe(self.conn, username, email)

    def unsubsribe_command(self, arguments : list[str], username : str) -> str:
        if not len(arguments) == 0:
            return 'Invalid number of arguments'

        return unsubscribe(self.conn, username)
    
    def help(self, arguments : list[str], username : str) -> str:
        if not len(arguments) == 0:
            return 'Invalid number of arguments'
        
        return """```
Supported commands are:
- get-top-news "preferences" "keywords"
- get-everything "keywords" "domain" "language" "sortBy" "pageSize"
- get-weather "city" "country"
- add-preference "preference"
- remove-preference "preference"
- subscribe "email"
- unsubscribe
- help

Additional Notes:
- Put a question mark as the first character to receive the output in DMs.
- Valid sortBys: "relevancy", "popularity", "publishedAt".
- Use 2-letter codes for languages.
- The name of the command should also be in quotes
- Supported preferences are business, entertainment, health, science,
sports, technology
```"""
    def execute_command(self, command : str, arguments : list[str], username : str) -> str:
        commands_dict = {'get-top-news' : self.get_top_user,
                        'get-everything' : self.get_everything_user, 
                        'get-weather' : self.get_weather,
                        'add-preference' : self.add_preference_command,
                        'remove-preference' : self.remove_preference_command,
                        'subscribe' : self.subsribe_command,
                        'unsubscribe' : self.unsubsribe_command,
                        'help' : self.help}

        if command not in commands_dict:
            return 'Unsupported command'

        return commands_dict[command](arguments, username)
