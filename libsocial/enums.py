from enum import Enum


class Category(str, Enum):
    All = "all"
    BugsProblems = "1"
    Suggestions = "2"
    TitlesSearch = "3"
    PersonnelSearch = "4"
    MangaDiscussion = "5"
    AnimeDiscussion = "6"
    RanobeDiscussion = "7"
    VideoGames = "8"
    Translators = "9"
    HowTranslateManga = "10"
    HowDrawManga = "11"
    Communication = "12"
    Others = "13"
