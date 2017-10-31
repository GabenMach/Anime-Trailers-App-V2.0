import media
import fresh_tomatoes

"""Requires fresh_tomatoes to make HTML page"""
# Create Movies
fate_zero = media.Movie("Fate Zero",
                        "https://i.pinimg.com/736x/40/ab/b6/40abb684119ea27ecb515714b42c5b22--fate-stay-night-fate-zero.jpg",
                        "https://www.youtube.com/watch?v=uLiyxXvW47o")
fate_apocrypha = media.Movie("Fate Apocrypha",
                             "https://i.pinimg.com/originals/c2/8a/18/c28a18fa91a4d4f001d1a97d6ea02175.jpg",
                             "https://www.youtube.com/watch?v=c2r3sF9vAGs")
kakegurui = media.Movie("Kakegurui",
                        "https://i.pinimg.com/originals/2a/f5/71/2af571929d03ff03226034e9ee75bcb3.jpg",
                        "https://www.youtube.com/watch?v=cTlHQiRNVl0")

# Open Movies
fresh_tomatoes.open_movies_page([kakegurui, fate_apocrypha, fate_zero])
