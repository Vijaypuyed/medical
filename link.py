from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.fitimage import FitImage
import webbrowser


from movies_data import movies  

KV = '''
ScreenManager:
    HomeScreen:
    DetailScreen:

<HomeScreen>:
    name: "home"

    BoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "🎬 Movies App"
            md_bg_color: 0.8, 0, 0, 1
            left_action_items: [["home", lambda x: app.go_home()]]

        FloatLayout:
            Carousel:
                id: movie_carousel
                direction: 'right'
                loop: True
                size_hint: 1, 0.7
                pos_hint: {"center_x":0.5, "center_y":0.45}

<DetailScreen>:
    name: "detail"
    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "10dp"

        MDTopAppBar:
            title: "Movie Details"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]

        FitImage:
            id: movie_poster
            size_hint_y: 0.5

        MDLabel:
            id: movie_title
            text: "Title"
            halign: "center"
            font_style: "H5"

        MDLabel:
            id: movie_year
            text: "Year"
            halign: "center"

        MDLabel:
            id: movie_genre
            text: "Genre"
            halign: "center"

        MDLabel:
            id: movie_desc
            text: "Description"
            halign: "center"
            theme_text_color: "Secondary"

        MDRaisedButton:
            text: "▶ Watch Trailer"
            pos_hint: {"center_x":0.5}
            on_release: app.open_trailer()
'''

class HomeScreen(Screen):
    pass

class DetailScreen(Screen):
    pass

class MovieTicketApp(MDApp):
    current_movie = {}

    def build(self):
        root = Builder.load_string(KV)
        carousel = root.get_screen("home").ids.movie_carousel

        # ✅ Load movies from external file
        for movie in movies:
            img = FitImage(source=movie["poster"])
            img.bind(on_touch_down=lambda inst, touch, m=movie: self.on_movie_click(inst, touch, m))
            carousel.add_widget(img)

        return root

    def on_movie_click(self, instance, touch, movie):
        if instance.collide_point(*touch.pos):
            self.show_movie_detail(movie)

    def show_movie_detail(self, movie):
        self.current_movie = movie
        detail_screen = self.root.get_screen("detail")
        detail_screen.ids.movie_title.text = movie["title"]
        detail_screen.ids.movie_year.text = f"Year: {movie['year']}"
        detail_screen.ids.movie_genre.text = f"Genre: {movie['genre']}"
        detail_screen.ids.movie_desc.text = movie["desc"]
        detail_screen.ids.movie_poster.source = movie["poster"]
        self.root.current = "detail"

    def open_trailer(self):
        if self.current_movie:
            webbrowser.open(self.current_movie["link"])

    def go_home(self):
        self.root.current = "home"

MovieTicketApp().run()
