import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from PIL import Image, ImageTk
from dropdown_menu import WineAppDropdownMenu

# Color palette
DARK_BURGUNDY = "#4A0E0E"
LIGHT_BURGUNDY = "#800020"
GOLD = "#FFD700"
CREAM = "#FFFDD0"


class WineAppMobileGUI:
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        self.root = ctk.CTk()
        self.root.title("Wine Enthusiast Profile")
        self.root.geometry("360x640")  # Common Android phone resolution

        self.colors = {
            "DARK_BURGUNDY": DARK_BURGUNDY,
            "LIGHT_BURGUNDY": LIGHT_BURGUNDY,
            "gold": GOLD,
            "cream": CREAM,
        }

        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        # Main content frame
        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color=self.colors["DARK_BURGUNDY"],
            border_width=2,
            border_color=self.colors["cream"],
        )
        self.main_frame.pack(fill="both", expand=True)

        # Add the dropdown menu
        self.dropdown_menu = WineAppDropdownMenu(
            self.main_frame, current_page=self.root
        )
        self.dropdown_menu.place(x=10, y=10)

        # Profile Photo
        self.photo_frame = ctk.CTkFrame(
            self.main_frame,
            width=120,
            height=120,
            corner_radius=60,
            fg_color=self.colors["DARK_BURGUNDY"],
        )
        self.photo_label = ctk.CTkLabel(
            self.photo_frame, text="", fg_color=self.colors["cream"]
        )
        self.photo_label.pack(expand=True, fill="both", padx=5, pady=5)

        # Name
        self.name_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Your Name",
            font=("Helvetica", 18),
            width=250,
            fg_color=self.colors["cream"],
            text_color=self.colors["DARK_BURGUNDY"],
        )

        # Favorite Wine
        self.fav_wine_entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Favorite Wine",
            font=("Helvetica", 14),
            width=250,
            fg_color=self.colors["cream"],
            text_color=self.colors["DARK_BURGUNDY"],
        )

        # About
        self.about_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.about_label = ctk.CTkLabel(
            self.about_frame,
            text="About Me",
            font=("Helvetica", 16, "bold"),
            text_color=self.colors["gold"],
        )
        self.about_text = ctk.CTkTextbox(
            self.about_frame,
            wrap="word",
            height=80,
            font=("Helvetica", 14),
            width=300,
            fg_color=self.colors["cream"],
            text_color=self.colors["DARK_BURGUNDY"],
        )
        self.about_text.insert("1.0", "Share your passion for wine...")

        # Last Reviews
        self.reviews_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.reviews_label = ctk.CTkLabel(
            self.reviews_frame,
            text="Recent Wine Reviews",
            font=("Helvetica", 16, "bold"),
            text_color=self.colors["gold"],
        )
        self.review1 = ctk.CTkLabel(
            self.reviews_frame,
            text="2022 Cabernet Sauvignon - Rich and full-bodied",
            font=("Helvetica", 14),
            fg_color=self.colors["cream"],
            corner_radius=8,
            pady=5,
        )
        self.review2 = ctk.CTkLabel(
            self.reviews_frame,
            text="2021 Chardonnay - Crisp with hints of oak",
            font=("Helvetica", 14),
            fg_color=self.colors["cream"],
            corner_radius=8,
            pady=5,
        )

        # Buttons
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.add_review_button = ctk.CTkButton(
            self.button_frame,
            text="Add Review",
            fg_color=self.colors["LIGHT_BURGUNDY"],
            hover_color=self.colors["gold"],
        )
        self.fav_button = ctk.CTkButton(
            self.button_frame,
            text="Favorites",
            fg_color=self.colors["LIGHT_BURGUNDY"],
            hover_color=self.colors["gold"],
        )
        self.edit_profile_button = ctk.CTkButton(
            self.button_frame,
            text="Edit Profile",
            fg_color=self.colors["LIGHT_BURGUNDY"],
            hover_color=self.colors["gold"],
        )

    def layout_widgets(self):
        self.photo_frame.place(relx=0.5, rely=0.15, anchor="center")
        self.name_entry.place(relx=0.5, rely=0.3, anchor="center")
        self.fav_wine_entry.place(relx=0.5, rely=0.38, anchor="center")

        self.about_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9)
        self.about_label.pack(anchor="w")
        self.about_text.pack(fill="x", pady=5)

        self.reviews_frame.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.9)
        self.reviews_label.pack(anchor="w", pady=(0, 5))
        self.review1.pack(fill="x", pady=2)
        self.review2.pack(fill="x", pady=2)

        self.button_frame.place(relx=0.5, rely=0.9, anchor="center", relwidth=0.9)
        self.add_review_button.pack(side="left", expand=True, padx=5)
        self.fav_button.pack(side="left", expand=True, padx=5)
        self.edit_profile_button.pack(side="right", expand=True, padx=5)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = WineAppMobileGUI()
    app.run()
