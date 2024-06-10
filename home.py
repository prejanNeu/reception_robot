import tkinter as tk
from PIL import Image, ImageTk

btn_width = 200
btn_height = 200

device_width = 1000
device_height = 600

arrow_width = 80
arrow_height = 80


def arrow_img():
    btn_image = Image.open("arrow.jpeg")
    max_size = (arrow_width, arrow_height)
    btn_image.thumbnail(max_size)
    btn_photo = ImageTk.PhotoImage(btn_image)
    return btn_photo


def open_courses():
    global root, bg_photo, arrow_image, new_window
    root.destroy()
    new_window = tk.Tk()
    new_window.title("Courses")
    course_im = Image.open("course.jpeg")
    course_img = course_im.resize((device_width, device_height))
    course_width, course_height = course_img.size
    canvas = tk.Canvas(new_window, width=course_width, height=course_height)
    canvas.pack()
    bg_photo = ImageTk.PhotoImage(course_img)
    canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)
    
    arrow_image = arrow_img()

    arrow = tk.Button(new_window, image=arrow_image, command=home_page, borderwidth=0)
    arrow.image = arrow_image  # Keep reference to avoid garbage collection
    canvas.create_window(10, 10, anchor=tk.NW, window=arrow)  # Positioning the arrow in the upper left corner
    
    new_window.mainloop()


def open_clubs():
    global root, new_window
    root.destroy()
    new_window = tk.Tk()
    new_window.title("Clubs")
    clubs_im = Image.open("club.jpeg")
    clubs_img = clubs_im.resize((device_width, device_height))
    clubs_width, clubs_height = clubs_img.size
    canvas = tk.Canvas(new_window, width=clubs_width, height=clubs_height)
    canvas.pack()
    bg_photo = ImageTk.PhotoImage(clubs_img)
    canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)
    arrow_image = arrow_img()
    
    arrow = tk.Button(new_window, image=arrow_image, command=home_page, borderwidth=0)
    arrow.image = arrow_image  # Keep reference to avoid garbage collection
    canvas.create_window(10, 10, anchor=tk.NW, window=arrow)  # Positioning the arrow in the upper left corner
    
    new_window.mainloop()


def open_faculty():
    global root, new_window
    root.destroy()
    new_window = tk.Tk()
    new_window.title("Faculty")
    faculty_im = Image.open("faculty.jpeg")
    faculty_img = faculty_im.resize((device_width, device_height))
    faculty_width, faculty_height = faculty_img.size
    canvas = tk.Canvas(new_window, width=faculty_width, height=faculty_height)
    canvas.pack()
    bg_photo = ImageTk.PhotoImage(faculty_img)
    canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)
    arrow_image = arrow_img()
    
    arrow = tk.Button(new_window, image=arrow_image, command=home_page, borderwidth=0)
    arrow.image = arrow_image  # Keep reference to avoid garbage collection
    canvas.create_window(10, 10, anchor=tk.NW, window=arrow)  # Positioning the arrow in the upper left corner
    
    new_window.mainloop()


def open_contact():
    global root, new_window
    root.destroy()
    new_window = tk.Tk()
    new_window.title("Contact")
    contact_im = Image.open("contact.jpeg")
    contact_img = contact_im.resize((device_width, device_height))
    contact_width, contact_height = contact_img.size
    canvas = tk.Canvas(new_window, width=contact_width, height=contact_height)
    canvas.pack()
    bg_photo = ImageTk.PhotoImage(contact_img)
    canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)

    arrow_image = arrow_img()
    
    arrow = tk.Button(new_window, image=arrow_image, command=home_page, borderwidth=0)
    arrow.image = arrow_image  # Keep reference to avoid garbage collection
    canvas.create_window(10, 10, anchor=tk.NW, window=arrow)  # Positioning the arrow in the upper left corner
    
    new_window.mainloop()


def course_img():
    btn_image = Image.open("1.jpeg")
    max_size = (btn_width, btn_height)
    btn_image.thumbnail(max_size)
    btn_photo = ImageTk.PhotoImage(btn_image)
    return btn_photo


def faculty_img():
    global bt
    btn_image = Image.open("2.jpeg")
    max_size = (btn_width, btn_height)
    btn_image.thumbnail(max_size)
    btn_photo = ImageTk.PhotoImage(btn_image)
    return btn_photo


def club_img():
    btn_image = Image.open("3.jpeg")
    max_size = (btn_width, btn_height)
    btn_image.thumbnail(max_size)
    btn_photo = ImageTk.PhotoImage(btn_image)
    return btn_photo


def contact_img():
    btn_image = Image.open("4.jpeg")
    max_size = (btn_width, btn_height)
    btn_image.thumbnail(max_size)
    btn_photo = ImageTk.PhotoImage(btn_image)
    return btn_photo


def create_background():
    global root, canvas, btn_img
    root = tk.Tk()
    root.title("Presidential Graduate School")
    
    # Load the background image
    image = Image.open("background.jpg")
    bg_image = image.resize((device_width, device_height))
    bg_width, bg_height = bg_image.size
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    # Create a canvas to place the background and button images
    canvas = tk.Canvas(root, width=bg_width, height=bg_height)
    canvas.pack()
    canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)

    # Create buttons and place them on the canvas
    button_commands = [open_courses, open_faculty, open_clubs, open_contact]
    button_titles = ["Courses", "Faculty", "Clubs", "Contact"]
    btn_img = [course_img(), faculty_img(), club_img(), contact_img()]

    for i, (command, title, btn_photo) in enumerate(zip(button_commands, button_titles, btn_img)):
        
        if i % 2 == 0:
            btn_x = (bg_width - btn_width) / 5.5
        else:
            btn_x = 3.5 * (bg_width - btn_width) / 4

        if i <= 1:
            btn_y = (bg_height - btn_height) / 1.5
        else:
            btn_y = 3 * (bg_height - btn_height) / 3
        btn = tk.Button(root, image=btn_photo, command=command, borderwidth=0)
        btn_window = canvas.create_window(btn_x, btn_y, anchor=tk.NW, window=btn)
        
    root.mainloop()


def home_page():
    new_window.destroy()
    

if __name__ == "__main__":
    while True:
        create_background()
