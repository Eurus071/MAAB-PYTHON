"""
Weather API and Movie Recommendation System
"""

import requests
import json
import random
from datetime import datetime
import os
from typing import Dict, List, Optional
import sys


WEATHER_API_KEY = "33f230140e4bd9ba7007efc3e73c3764"  #  https://openweathermap.org/api
MOVIE_API_KEY = ""           # https://www.themoviedb.org/settings/api

FALLBACK_MOVIES = {
    "Action": [
        {"title": "The Dark Knight", "year": 2008, "overview": "Batman faces the Joker in Gotham City."},
        {"title": "Mad Max: Fury Road", "year": 2015, "overview": "A post-apocalyptic action film."},
        {"title": "John Wick", "year": 2014, "overview": "An ex-hitman seeks revenge."}
    ],
    "Comedy": [
        {"title": "The Grand Budapest Hotel", "year": 2014, "overview": "Adventures of a concierge and his lobby boy."},
        {"title": "Superbad", "year": 2007, "overview": "High school friends try to buy alcohol for a party."},
        {"title": "Bridesmaids", "year": 2011, "overview": "A maid of honor plans her friend's wedding."}
    ],
    "Drama": [
        {"title": "The Shawshank Redemption", "year": 1994, "overview": "Two imprisoned men bond over years."},
        {"title": "Forrest Gump", "year": 1994, "overview": "A man with low IQ witnesses historical events."},
        {"title": "The Godfather", "year": 1972, "overview": "The aging patriarch of a crime family transfers control."}
    ],
    "Science Fiction": [
        {"title": "Inception", "year": 2010, "overview": "A thief steals corporate secrets through dream-sharing."},
        {"title": "The Matrix", "year": 1999, "overview": "A hacker discovers the truth about his reality."},
        {"title": "Interstellar", "year": 2014, "overview": "Explorers travel through a wormhole in space."}
    ],
    "Horror": [
        {"title": "Get Out", "year": 2017, "overview": "A young African-American visits his white girlfriend's parents."},
        {"title": "Hereditary", "year": 2018, "overview": "A family unravels after the death of their grandmother."},
        {"title": "The Conjuring", "year": 2013, "overview": "Paranormal investigators help a family terrorized by a dark presence."}
    ]
}


GENRE_MAPPING = {
    "action": 28,
    "adventure": 12,
    "comedy": 35,
    "drama": 18,
    "horror": 27,
    "romance": 10749,
    "science fiction": 878,
    "thriller": 53,
    "animation": 16,
    "fantasy": 14
}

# ============================================================================
# TASK 1: WEATHER API
# ============================================================================

class WeatherApp:
    """Weather application using OpenWeatherMap API"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or WEATHER_API_KEY
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.units = "metric" 
        
    def get_weather(self, city: str, country_code: str = None) -> Optional[Dict]:
        """
        Fetch weather data for a specific city
        
        Args:
            city: City name
            country_code: Optional country code (e.g., 'US', 'UZ')
            
        Returns:
            Dictionary containing weather data or None if error
        """
        if not self.api_key or self.api_key == "33f230140e4bd9ba7007efc3e73c3764":
            print("  Weather API key not set. Please get a free API key from:")
            print("   https://openweathermap.org/api")
            print("   Then replace WEATHER_API_KEY in the code with your key.")
            return None

        params = {
            "q": f"{city},{country_code}" if country_code else city,
            "appid": self.api_key,
            "units": self.units,
            "lang": "en"
        }
        
        try:
            print(f"Fetching weather data for {city}...")
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return data
            
        except requests.exceptions.RequestException as e:
            print(f" Error fetching weather data: {e}")
            return None
        except json.JSONDecodeError:
            print(" Error parsing weather data")
            return None
    
    def display_weather(self, weather_data: Dict) -> None:
        """
        Display weather information in a user-friendly format
        
        Args:
            weather_data: Weather data dictionary from API
        """
        if not weather_data:
            print("No weather data available")
            return
        
        try:
            city = weather_data.get("name", "Unknown")
            country = weather_data.get("sys", {}).get("country", "")
            temp = weather_data.get("main", {}).get("temp", 0)
            feels_like = weather_data.get("main", {}).get("feels_like", 0)
            humidity = weather_data.get("main", {}).get("humidity", 0)
            pressure = weather_data.get("main", {}).get("pressure", 0)
            description = weather_data.get("weather", [{}])[0].get("description", "").title()
            wind_speed = weather_data.get("wind", {}).get("speed", 0)
            clouds = weather_data.get("clouds", {}).get("all", 0)

            sunrise_ts = weather_data.get("sys", {}).get("sunrise", 0)
            sunset_ts = weather_data.get("sys", {}).get("sunset", 0)
            
            if sunrise_ts:
                sunrise = datetime.fromtimestamp(sunrise_ts).strftime("%H:%M")
            else:
                sunrise = "N/A"
                
            if sunset_ts:
                sunset = datetime.fromtimestamp(sunset_ts).strftime("%H:%M")
            else:
                sunset = "N/A"

            print("\n" + "=" * 50)
            print(f"WEATHER FOR {city.upper()}, {country}")
            print("=" * 50)
            
            print(f"\n Temperature: {temp:.1f}°C (Feels like: {feels_like:.1f}°C)")
            print(f" Condition: {description}")
            print(f" Humidity: {humidity}%")
            print(f" Pressure: {pressure} hPa")
            print(f" Wind Speed: {wind_speed} m/s")
            print(f"  Cloudiness: {clouds}%")
            print(f" Sunrise: {sunrise}")
            print(f" Sunset: {sunset}")
            
            # Additional weather details
            if "rain" in weather_data:
                rain_volume = weather_data["rain"].get("1h", 0)
                print(f" Rain (last hour): {rain_volume} mm")
            
            if "snow" in weather_data:
                snow_volume = weather_data["snow"].get("1h", 0)
                print(f" Snow (last hour): {snow_volume} mm")
            
            print("\n" + "=" * 50)
            
        except Exception as e:
            print(f" Error displaying weather data: {e}")
    
    def run_weather_app(self) -> None:
        """Interactive weather application"""
        print("\n" + "=" * 60)
        print("WEATHER APPLICATION")
        print("=" * 60)
        
        while True:
            print("\nOptions:")
            print("1. Check weather for a city")
            print("2. Check weather for multiple cities")
            print("3. Return to main menu")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                city = input("Enter city name: ").strip()
                if not city:
                    print(" City name cannot be empty")
                    continue
                
                country = input("Enter country code (optional, e.g., US, UZ): ").strip()
                
                weather_data = self.get_weather(city, country if country else None)
                
                if weather_data:
                    self.display_weather(weather_data)
                else:
                    print(f" Could not fetch weather data for {city}")

                    print("\n Sample weather data (for demonstration):")
                    sample_data = {
                        "name": city,
                        "sys": {"country": country or "??"},
                        "main": {
                            "temp": 22.5,
                            "feels_like": 23.0,
                            "humidity": 65,
                            "pressure": 1013
                        },
                        "weather": [{"description": "clear sky"}],
                        "wind": {"speed": 3.5},
                        "clouds": {"all": 20},
                        "sys": {"sunrise": 1678683600, "sunset": 1678726800}
                    }
                    self.display_weather(sample_data)
            
            elif choice == '2':
                cities_input = input("Enter city names separated by commas: ").strip()
                cities = [city.strip() for city in cities_input.split(",") if city.strip()]
                
                if not cities:
                    print(" No cities entered")
                    continue
                
                print(f"\nFetching weather for {len(cities)} cities...")
                for city in cities:
                    print(f"\n{'─' * 30}")
                    weather_data = self.get_weather(city)
                    
                    if weather_data:
                        temp = weather_data.get("main", {}).get("temp", 0)
                        desc = weather_data.get("weather", [{}])[0].get("description", "").title()
                        print(f"{city}: {temp:.1f}°C, {desc}")
                    else:
                        print(f"{city}: Data unavailable")
            
            elif choice == '3':
                print("Returning to main menu...")
                break
            
            else:
                print(" Invalid choice. Please try again.")

# ============================================================================
# TASK 2: MOVIE RECOMMENDATION SYSTEM
# ============================================================================

class MovieRecommender:
    """Movie recommendation system using TMDB API"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or MOVIE_API_KEY
        self.base_url = "https://api.themoviedb.org/3"
        self.headers = {"accept": "application/json"}
        self.cached_genres = {}
        
    def get_genre_id(self, genre_name: str) -> Optional[int]:
        """
        Get TMDB genre ID from genre name
        
        Args:
            genre_name: Genre name (e.g., "action", "comedy")
            
        Returns:
            Genre ID or None if not found
        """

        genre_lower = genre_name.lower()
        if genre_lower in GENRE_MAPPING:
            return GENRE_MAPPING[genre_lower]

        if self.api_key and self.api_key != "TMDB_API_KEY_HERE":
            try:
                url = f"{self.base_url}/genre/movie/list"
                params = {"api_key": self.api_key, "language": "en-US"}
                
                response = requests.get(url, params=params, headers=self.headers, timeout=10)
                response.raise_for_status()
                
                genres_data = response.json().get("genres", [])
                
                for genre in genres_data:
                    self.cached_genres[genre["name"].lower()] = genre["id"]
                
                return self.cached_genres.get(genre_lower)
                
            except Exception as e:
                print(f"  Could not fetch genres from API: {e}")
        
        return None
    
    def get_movies_by_genre(self, genre_id: int, page: int = 1) -> Optional[List[Dict]]:
        """
        Fetch movies by genre ID
        
        Args:
            genre_id: TMDB genre ID
            page: Page number for pagination
            
        Returns:
            List of movie dictionaries or None if error
        """
        if not self.api_key or self.api_key == "YOUR_TMDB_API_KEY_HERE":
            print("  Movie API key not set. Using fallback data.")
            print("   To use the real API, get a free API key from:")
            print("   https://www.themoviedb.org/settings/api")
            print("   Then replace MOVIE_API_KEY in the code with your key.")
            return None
        
        try:
            url = f"{self.base_url}/discover/movie"
            params = {
                "api_key": self.api_key,
                "with_genres": genre_id,
                "page": page,
                "language": "en-US",
                "sort_by": "popularity.desc"
            }
            
            print(f" Fetching movies from page {page}...")
            response = requests.get(url, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return data.get("results", [])
            
        except requests.exceptions.RequestException as e:
            print(f" Error fetching movies: {e}")
            return None
        except json.JSONDecodeError:
            print(" Error parsing movie data")
            return None
    
    def get_random_movie(self, genre_name: str) -> Optional[Dict]:
        """
        Get a random movie from the specified genre
        
        Args:
            genre_name: Genre name
            
        Returns:
            Movie dictionary or None if error
        """
        print(f"\nLooking for {genre_name} movies...")
        genre_id = self.get_genre_id(genre_name)
        
        if not genre_id:
            print(f" Genre '{genre_name}' not found. Available genres:")
            print(", ".join(GENRE_MAPPING.keys()))
            return None

        movies = self.get_movies_by_genre(genre_id)

        if not movies:
            print("  Using fallback movie data for demonstration")

            for fallback_genre, fallback_movies in FALLBACK_MOVIES.items():
                if genre_name.lower() in fallback_genre.lower():
                    if fallback_movies:
                        movie = random.choice(fallback_movies)
                        return {
                            "title": movie["title"],
                            "overview": movie["overview"],
                            "release_date": str(movie["year"]),
                            "vote_average": random.uniform(6.0, 9.0),
                            "popularity": random.uniform(50, 100)
                        }

            all_fallback_movies = []
            for genre_movies in FALLBACK_MOVIES.values():
                all_fallback_movies.extend(genre_movies)
            
            if all_fallback_movies:
                movie = random.choice(all_fallback_movies)
                return {
                    "title": movie["title"],
                    "overview": movie["overview"],
                    "release_date": str(movie["year"]),
                    "vote_average": random.uniform(6.0, 9.0),
                    "popularity": random.uniform(50, 100)
                }
            
            return None

        valid_movies = [m for m in movies if m.get("title") and m.get("overview")]
        
        if not valid_movies:
            print("❌ No valid movies found in this genre")
            return None

        return random.choice(valid_movies)
    
    def display_movie(self, movie: Dict) -> None:
        """
        Display movie information in a user-friendly format
        
        Args:
            movie: Movie dictionary
        """
        if not movie:
            print(" No movie data to display")
            return
        
        print("\n" + "=" * 60)
        print(" YOUR MOVIE RECOMMENDATION")
        print("=" * 60)
        
        title = movie.get("title", "Unknown Title")
        overview = movie.get("overview", "No description available.")
        release_date = movie.get("release_date", "Unknown year")
        rating = movie.get("vote_average", "N/A")
        popularity = movie.get("popularity", "N/A")

        if release_date and len(release_date) >= 4:
            year = release_date[:4]
        else:
            year = "Unknown"
        
        print(f"\n Title: {title} ({year})")
        print(f"Rating: {rating}/10")
        print(f"Popularity Score: {popularity:.1f}")
        print(f"\n Synopsis:\n{overview}")
        
        # Additional information if available
        if "genres" in movie and movie["genres"]:
            genre_names = [g["name"] for g in movie["genres"]]
            print(f"\n Genres: {', '.join(genre_names)}")
        
        if "runtime" in movie and movie["runtime"]:
            hours = movie["runtime"] // 60
            minutes = movie["runtime"] % 60
            print(f"Runtime: {hours}h {minutes}m")
        
        print("\n" + "=" * 60)
    
    def run_movie_recommender(self) -> None:
        """Interactive movie recommendation application"""
        print("\n" + "=" * 60)
        print("MOVIE RECOMMENDATION SYSTEM")
        print("=" * 60)
        
        print("\n Available genres:")
        genres_list = list(GENRE_MAPPING.keys())
        for i, genre in enumerate(genres_list, 1):
            print(f"  {i}. {genre.title()}")
        
        while True:
            print("\nOptions:")
            print("1. Get movie recommendation by genre")
            print("2. Get multiple recommendations")
            print("3. List all available genres")
            print("4. Return to main menu")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                genre_input = input("Enter genre name: ").strip().lower()
                
                if not genre_input:
                    print(" Genre name cannot be empty")
                    continue
                
                movie = self.get_random_movie(genre_input)
                
                if movie:
                    self.display_movie(movie)

                    another = input("\n🎬 Get another recommendation from same genre? (y/n): ").strip().lower()
                    if another == 'y':
                        movie2 = self.get_random_movie(genre_input)
                        if movie2 and movie2.get("title") != movie.get("title"):
                            self.display_movie(movie2)
                else:
                    print(f" Could not find movies in genre '{genre_input}'")
                    print("   Try: action, comedy, drama, horror, science fiction, etc.")
            
            elif choice == '2':
                print("Get recommendations for multiple genres")
                genres_input = input("Enter genres separated by commas: ").strip()
                genres = [g.strip().lower() for g in genres_input.split(",") if g.strip()]
                
                if not genres:
                    print(" No genres entered")
                    continue
                
                print(f"\nGetting recommendations for {len(genres)} genres...")
                recommended_movies = []
                
                for genre in genres:
                    movie = self.get_random_movie(genre)
                    if movie and movie.get("title"):
                        if not any(m.get("title") == movie.get("title") for m in recommended_movies):
                            recommended_movies.append(movie)
                
                if recommended_movies:
                    print(f"\n🎬 Found {len(recommended_movies)} recommendations:")
                    for i, movie in enumerate(recommended_movies, 1):
                        title = movie.get("title", "Unknown")
                        year = movie.get("release_date", "????")[:4] if movie.get("release_date") else "????"
                        rating = movie.get("vote_average", "N/A")
                        print(f"  {i}. {title} ({year}) - ⭐ {rating}/10")

                    try:
                        choice_num = input("\nEnter number to see details (or press Enter to skip): ").strip()
                        if choice_num and choice_num.isdigit():
                            idx = int(choice_num) - 1
                            if 0 <= idx < len(recommended_movies):
                                self.display_movie(recommended_movies[idx])
                    except ValueError:
                        pass
                else:
                    print(" No movies found for the specified genres")
            
            elif choice == '3':
                print("\n Available genres:")
                print("-" * 30)
                for genre in sorted(GENRE_MAPPING.keys()):
                    print(f"  • {genre.title()}")
                print("\n Tip: You can also try combining genres (e.g., 'action comedy')")
            
            elif choice == '4':
                print("Returning to main menu...")
                break
            
            else:
                print(" Invalid choice. Please try again.")

def check_api_keys():
    """Check if API keys are set and provide instructions"""
    print("\n API KEY STATUS")
    print("-" * 40)
    
    weather_status = " Set" if WEATHER_API_KEY != "33f230140e4bd9ba7007efc3e73c3764" else " Not Set"
    movie_status = " Set" if MOVIE_API_KEY != "YOUR_TMDB_API_KEY_HERE" else " Not Set"
    
    print(f"Weather API Key: {weather_status}")
    print(f"Movie API Key: {movie_status}")
    
    if weather_status == " Not Set" or movie_status == " Not Set":
        print("\n IMPORTANT:")
        print("For full functionality, you need to:")
        
        if weather_status == " Not Set":
            print("1. Get a FREE Weather API key from: https://openweathermap.org/api")
            print("2. Replace '33f230140e4bd9ba7007efc3e73c3764' with your key")
        
        if movie_status == " Not Set":
            print("3. Get a FREE Movie API key from: https://www.themoviedb.org/settings/api")
            print("4. Replace 'YOUR_TMDB_API_KEY_HERE' with your key")
        
        print("\nThe program will work with sample data, but real API data is better!")
        input("\nPress Enter to continue with sample data...")

def main():
    """Main application menu"""
    print("=" * 70)
    print("WEATHER & MOVIE RECOMMENDATION SYSTEM")
    print("=" * 70)

    check_api_keys()

    weather_app = WeatherApp()
    movie_recommender = MovieRecommender()
    
    while True:
        print("\n" + "=" * 60)
        print("MAIN MENU")
        print("=" * 60)
        print("1.  Weather Application")
        print("2.  Movie Recommendation System")
        print("3.  Run Both Applications")
        print("4.  Check API Key Status")
        print("5.  Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            weather_app.run_weather_app()
        
        elif choice == '2':
            movie_recommender.run_movie_recommender()
        
        elif choice == '3':
            print("\n" + "=" * 70)
            print("RUNNING BOTH APPLICATIONS")
            print("=" * 70)

            print("\n Starting Weather Application...")
            weather_app.run_weather_app()
            
            input("\nPress Enter to continue to Movie Recommendations...")

            print("\n Starting Movie Recommendation System...")
            movie_recommender.run_movie_recommender()
        
        elif choice == '4':
            check_api_keys()
        
        elif choice == '5':
            print("\n" + "=" * 60)
            print("Thank you for using the application!")
            print("=" * 60)
            break
        
        else:
            print(" Invalid choice. Please try again.")

def run_demo():
    """Run a quick demonstration of both applications"""
    print("=" * 70)
    print("DEMONSTRATION MODE")
    print("=" * 70)

    weather_app = WeatherApp()
    movie_recommender = MovieRecommender()
    
    print("\n1.   WEATHER DEMO (using sample data)")
    print("-" * 40)

    print("\nSample weather for Tashkent, Uzbekistan:")
    sample_weather = {
        "name": "Tashkent",
        "sys": {"country": "UZ"},
        "main": {
            "temp": 25.5,
            "feels_like": 26.0,
            "humidity": 45,
            "pressure": 1015
        },
        "weather": [{"description": "sunny"}],
        "wind": {"speed": 2.1},
        "clouds": {"all": 10},
        "sys": {"sunrise": 1678683600, "sunset": 1678726800}
    }
    weather_app.display_weather(sample_weather)
    
    print("\n2.  MOVIE RECOMMENDATION DEMO")
    print("-" * 40)

    genres_to_try = ["action", "comedy", "science fiction"]
    for genre in genres_to_try:
        print(f"\nTrying genre: {genre.title()}")
        movie = movie_recommender.get_random_movie(genre)
        if movie:
            print(f"  Recommended: {movie.get('title', 'Unknown')}")
        else:
            print(f"  No movie found for {genre}")

    print("\nDetailed recommendation for 'Action':")
    action_movie = movie_recommender.get_random_movie("action")
    if action_movie:
        movie_recommender.display_movie(action_movie)
    
    print("\n" + "=" * 70)
    print("DEMO COMPLETE!")
    print("=" * 70)
    print("\nFor full functionality with real data:")
    print("1. Get API keys as shown above")
    print("2. Replace the API key placeholders in the code")
    print("3. Run the main() function")
if __name__ == "__main__":
    print("Welcome to the Weather & Movie Recommendation System!")
    print("\nChoose mode:")
    print("1. Run main application (interactive)")
    print("2. Run quick demonstration")
    
    mode = input("\nEnter choice (1 or 2): ").strip()
    
    if mode == '2':
        run_demo()
    else:
        main()