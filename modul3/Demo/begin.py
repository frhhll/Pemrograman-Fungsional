from functools import reduce

# Data movies
movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

# Menampilkan data dari film yang dipilih
def show_movie_info(movie):
    print(f"Title: {movie['title']}, Year: {movie['year']}, Rating: {movie['rating']}, Genre: {movie['genre']}")

# Jumlah film berdasarkan genre
def count_movies_by_genre(movies):
    genre_counts = {}
    for movie in movies:
        genre = movie["genre"]
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts

# Rata-rata rating film berdasarkan tahun rilis
def average_rating_by_year(movies):
    rating_sum_by_year = {}
    rating_count_by_year = {}
    for movie in movies:
        year = movie["year"]
        rating = movie["rating"]
        rating_sum_by_year[year] = rating_sum_by_year.get(year, 0) + rating
        rating_count_by_year[year] = rating_count_by_year.get(year, 0) + 1
    return {year: rating_sum_by_year[year] / rating_count_by_year[year] for year in rating_sum_by_year}

# Film dengan rating tertinggi
def movie_with_highest_rating(movies):
    return max(movies, key=lambda x: x["rating"])

# Mencari judul film untuk menampilkan informasi rating, tahun rilis, dan genre
def find_movie_by_title(movies, title):
    for movie in movies:
        if movie["title"].lower() == title.lower():
            return movie
    return None

# Looping untuk mengikuti alur interaksi yang diminta
while True:
    print("\nMenu Tugas:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")
    task = input("Masukkan nomor tugas (1/2/3/4/5): ")

    if task == "1":
        genre_counts = count_movies_by_genre(movies)
        print(f"Jumlah Film Berdasarkan Genre: {genre_counts}")
    elif task == "2":
        average_ratings = average_rating_by_year(movies)
        print(f"Rata-rata Rating Film Berdasarkan Tahun Rilis: {average_ratings}")
    elif task == "3":
        highest_rated_movie = movie_with_highest_rating(movies)
        print("\nFilm dengan Rating Tertinggi:")
        show_movie_info(highest_rated_movie)
    elif task == "4":
        title = input("Masukkan judul film yang ingin dicari: ")
        found_movie = find_movie_by_title(movies, title)
        if found_movie:
            print("\nInformasi Film:")
            show_movie_info(found_movie)
        else:
            print("\nFilm dengan judul tersebut tidak ditemukan.")
    elif task == "5":
        print("Program Selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")