from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.fitimage import FitImage
import webbrowser

KV = '''
ScreenManager:
    HomeScreen:
    DetailScreen:
    LoginScreen:
    RegistrationScreen:
    AboutScreen: 

<HomeScreen>:
    name: "home"

    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "🎬 Movies App"
            md_bg_color: 0.8, 0, 0, 1
            left_action_items: [["home", lambda x: app.go_home()]]
            right_action_items: [["login", lambda x: app.go_login()], ["account-plus", lambda x: app.go_register()], ["information", lambda x: app.go_about()]]

        FloatLayout:
            FitImage:
                source: "netflix_bg.jpg"
                allow_stretch: True
                keep_ratio: False

            Carousel:
                id: movie_carousel
                direction: 'right'
                loop: True
                size_hint: 1, 0.7
                pos_hint: {"center_x":0.5, "center_y":0.45}

                FitImage:
                    source: "https://m.media-amazon.com/images/I/51nbVEuw1HL._AC_.jpg"

                FitImage:
                    source: "https://m.media-amazon.com/images/I/51k0qa6qH1L._AC_.jpg"

                FitImage:
                    source: "https://m.media-amazon.com/images/I/71n58cBL2jL._AC_SL1024_.jpg"


<AboutScreen>:   # 👈 New screen
    name: "about"
    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "20dp"

        MDTopAppBar:
            title: "ℹ About This App"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]

        MDLabel:
            text: "Welcome to the Movies Ticket App!"
            halign: "center"
            font_style: "H5"

        MDLabel:
            text: "This app lets you browse movies, watch trailers, and book tickets."
            halign: "center"
            theme_text_color: "Secondary"

        MDRaisedButton:
            text: "Back to Home"
            pos_hint: {"center_x":0.5}
            on_release: app.go_home()
<LoginScreen>:
    name: "login"
    BoxLayout:
        orientation: "vertical"
        spacing: 20
        padding: 50

        MDLabel:
            text: "Login"
            halign: "center"
            font_style: "H4"

        MDTextField:
            hint_text: "Username"
            helper_text: "Enter your username"
            helper_text_mode: "on_focus"

        MDTextField:
            hint_text: "Password"
            password: True
            helper_text: "Enter your password"
            helper_text_mode: "on_focus"

        BoxLayout:
            size_hint_y: None
            height: "40dp"
            spacing: 20

            MDRaisedButton:
                text: "Forgot ID"
                on_release: app.forgot_id()

            MDRaisedButton:
                text: "Forgot Password"
                on_release: app.forgot_password()

      

<LoginScreen>:
    name: "login"
    BoxLayout:
        orientation: "vertical"
        spacing: 20
        padding: 50

        MDLabel:
            text: "Login"
            halign: "center"
            font_style: "H4"

        MDTextField:
            hint_text: "Username"
            helper_text: "Enter your username"
            helper_text_mode: "on_focus"

        MDTextField:
            hint_text: "Password"
            password: True
            helper_text: "Enter your password"
            helper_text_mode: "on_focus"

        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x":0.5}
            on_release: app.go_home()

<RegistrationScreen>:
    name: "register"
    
    BoxLayout:
        orientation: "vertical"
        spacing: 20
        padding: 50

        MDLabel:
            text: "Register"
            halign: "center"
            font_style: "H4"

        MDTextField:
            hint_text: "Full Name"

        MDTextField:
            hint_text: "Email"

        MDTextField:
            hint_text: "Password"
            password: True

        MDRaisedButton:
            text: "Register"
            pos_hint: {"center_x":0.5}
            on_release: app.go_home()
'''

class HomeScreen(Screen):
    pass

class DetailScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class RegistrationScreen(Screen):
    pass
class AboutScreen(Screen):
    pass
class MovieTicketApp(MDApp):
    
    current_movie = {}
    movies = [
        {
            "title": "Inception",
            "year": "2010",
            "genre": "Sci-Fi",
            "desc": "A thief who steals corporate secrets through dream-sharing.",
            "link": "https://www.youtube.com/watch?v=YoHD9XEInc0",
            "poster": "https://m.media-amazon.com/images/I/51nbVEuw1HL._AC_.jpg"
        },
        {
            "title": "The Dark Knight",
            "year": "2008",
            "genre": "Action",
            "desc": "Batman faces the Joker in Gotham City.",
            "link": "https://www.youtube.com/watch?v=EXeTwQWrcwY",
            "poster": "https://m.media-amazon.com/images/I/51k0qa6qH1L._AC_.jpg"
        }
    ]

    def build(self):
        root = Builder.load_string(KV)
        carousel = root.get_screen("home").ids.movie_carousel

        # Add movies to carousel
        for movie in self.movies:
            img = FitImage(source=movie["poster"])
            img.bind(on_touch_down=lambda inst, touch, m=movie: self.on_movie_click(inst, touch, m))
            carousel.add_widget(img)

        return root
    
    # Movie poster click
    def on_movie_click(self, instance, touch, movie):
        if instance.collide_point(*touch.pos):
            self.show_movie_detail(movie)

    # Show movie detail
    def show_movie_detail(self, movie):
        self.current_movie = movie
        detail_screen = self.root.get_screen("detail")
        detail_screen.ids.movie_title.text = movie["title"]
        detail_screen.ids.movie_year.text = f"Year: {movie['year']}"
        detail_screen.ids.movie_genre.text = f"Genre: {movie['genre']}"
        detail_screen.ids.movie_desc.text = movie["desc"]
        detail_screen.ids.movie_poster.source = movie["poster"]
        self.root.current = "detail"

    # Open trailer
    def open_trailer(self):
        if self.current_movie:
            webbrowser.open(self.current_movie["link"])

    # Book ticket
    def book_ticket(self):
        if self.current_movie:
            print(f"🎫 Ticket booked for {self.current_movie['title']}!")

    # Navigation
    def go_home(self):
        self.root.current = "home"

    def go_login(self):
        self.root.current = "login"

    def go_register(self):
        self.root.current = "register"

    def forgot_id(self):
        print("Forgot ID clicked!")  

    def go_about(self):
        self.root.current = "about"


    def forgot_password(self):
        print("Forgot Password clicked!") 

MovieTicketApp().run()
