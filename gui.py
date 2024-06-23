import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from tkinter import ttk
import os


class CapperGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Capper GUI")
        self.geometry("800x800")

        self.image_path = tk.StringVar()
        self.hex_color = tk.StringVar()
        self.base_filename = tk.StringVar(value="caption")
        self.output_directory = tk.StringVar(value="output")
        self.img_height = tk.StringVar(value="auto")

        self.create_widgets()

    def create_widgets(self):
        self.create_image_section()
        self.create_output_section()
        self.create_characters_section()
        self.create_text_section()
        self.create_credits_section()
        self.create_buttons_section()
    
    def create_image_section(self):
        image_frame = tk.LabelFrame(self, text="Image")
        image_frame.pack(fill="x", padx=10, pady=5)

        browse_btn = tk.Button(image_frame, text="Browse Image", command=self.browse_image)
        browse_btn.pack(side="left", padx=5)

        self.image_path_label = tk.Label(image_frame, textvariable=self.image_path, wraplength=300)
        self.image_path_label.pack(side="left", padx=5, fill="x", expand=True)

        self.color_label = tk.Label(image_frame, text="Pick Color")
        self.color_label.pack(side="left", padx=5, pady=10)
        color_btn = tk.Button(image_frame, text="Choose Color", command=self.choose_color)
        color_btn.pack(side="left", padx=5, pady=10)

        img_height_label = tk.Label(image_frame, text="Image Height")
        img_height_label.pack(side="left", padx=5)
        self.img_height_entry = tk.Entry(image_frame, textvariable=self.img_height)
        self.img_height_entry.pack(side="left", padx=5)

    def create_output_section(self):
        output_frame = tk.LabelFrame(self, text="Output")
        output_frame.pack(fill="x", padx=10, pady=5)

        base_filename_label = tk.Label(output_frame, text="Base Filename")
        base_filename_label.pack(side="left", padx=5)
        self.base_filename_entry = tk.Entry(output_frame, textvariable=self.base_filename)
        self.base_filename_entry.pack(side="left", padx=5)

        output_dir_label = tk.Label(output_frame, text="Output Directory")
        output_dir_label.pack(side="left", padx=5)
        self.output_dir_entry = tk.Entry(output_frame, textvariable=self.output_directory)
        self.output_dir_entry.pack(side="left", padx=5)
        
        self.caption_var = tk.IntVar(value=1)
        self.caption_chk = tk.Checkbutton(output_frame, text="Caption", variable=self.caption_var)
        self.caption_chk.pack(side="left", padx=5)
        
        self.autospec_var = tk.IntVar(value=0)
        self.autospec_chk = tk.Checkbutton(output_frame, text="Autospec", variable=self.autospec_var)
        self.autospec_chk.pack(side="left", padx=5)

        self.credits_var = tk.IntVar(value=0)
        self.credits_chk = tk.Checkbutton(output_frame, text="Credits", variable=self.credits_var)
        self.credits_chk.pack(side="left", padx=5)

    def create_characters_section(self):
        characters_frame = tk.LabelFrame(self, text="Characters")
        characters_frame.pack(fill="x", padx=10, pady=5)
        self.character_entries = []
        self.add_character_entries(characters_frame)
        self.character_entries[0][0].insert(0, "serif") # set default name of first "character" to serif font
        self.character_entries[0][1].insert(0, "#000000") # set default color to black
        self.character_entries[0][1].config(bg="#000000")
        self.character_entries[0][2].insert(0, "fonts/Noto_Serif/NotoSerif-Regular.ttf") # set default font to serif
        self.add_char_button = tk.Button(characters_frame, text="+", command=lambda: self.add_character_entries(characters_frame))
        self.add_char_button.pack(side="top", pady=5)

    def create_text_section(self):
        text_frame = tk.LabelFrame(self, text="Text")
        text_frame.pack(fill="x", padx=10, pady=5)

        text_frame_inner = tk.Frame(text_frame)
        text_frame_inner.pack(fill="x", padx=5)

        self.text_input = tk.Text(text_frame_inner, height=10, wrap="word")
        self.text_input.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(text_frame_inner, orient="vertical", command=self.text_input.yview)
        self.text_input.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        text_loc_label = tk.Label(text_frame, text="Caption Text Location")
        text_loc_label.pack(side="left", padx=5)

        self.text_loc_var = tk.StringVar(value="left")
        self.text_loc_menu = ttk.Combobox(text_frame, textvariable=self.text_loc_var, values=["left", "right", "split"])
        self.text_loc_menu.pack(side="left", padx=5, pady=10)

        align_label = tk.Label(text_frame, text="Text Alignment")
        align_label.pack(side="left", padx=5)

        self.align_var = tk.StringVar(value="center")
        self.align_menu = ttk.Combobox(text_frame, textvariable=self.align_var, values=["left", "right", "center"])
        self.align_menu.pack(side="left", padx=5, pady=10)

    def create_credits_section(self):
        credits_frame = tk.LabelFrame(self, text="Credits")
        credits_frame.pack(fill="x", padx=10, pady=5)

        credits_frame_inner = tk.Frame(credits_frame)
        credits_frame_inner.pack(fill="x", padx=5)

        self.credits_input = tk.Text(credits_frame_inner, height=4, width=5, wrap="word")
        self.credits_input.pack(side="left", fill="both", expand=True)

        cred_align_label = tk.Label(credits_frame, text="Credits Location")
        cred_align_label.pack(side="left", padx=5)

        self.cred_align_var = tk.StringVar(value="tl")
        self.cred_align_menu = ttk.Combobox(credits_frame, textvariable=self.cred_align_var, values=["tl", "tr", "bl", "br"])
        self.cred_align_menu.pack(side="left", padx=5, pady=10)

    def create_buttons_section(self):
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(fill="x", padx=10, pady=5)

        export_toml_btn = tk.Button(buttons_frame, text="Export TOML", command=self.export_TOML)
        export_toml_btn.pack(side="left", padx=5)

        #load_project_btn = tk.Button(buttons_frame, text="Load Project", command=self.load_project)
        #load_project_btn.pack(side="left", padx=5)

        generate_btn = tk.Button(buttons_frame, text="Generate", command=self.generate_output)
        generate_btn.pack(side="left", padx=5)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.image_path.set(file_path)
    
    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code[1]:
            self.hex_color.set(color_code[1])
            self.color_label.config(bg=color_code[1])

            
    def add_character_entries(self, parent):
        frame = tk.Frame(parent)
        frame.pack(fill="x", pady=5)

        name_label = tk.Label(frame, text="Name")
        name_label.pack(side="left", padx=5)
        name_entry = tk.Entry(frame)
        name_entry.pack(side="left", padx=5)

        color_label = tk.Label(frame, text="Color")
        color_label.pack(side="left", padx=5)
        color_entry = tk.Entry(frame)
        color_btn = tk.Button(frame, text="Choose", command=lambda: self.choose_char_color(color_entry))
        color_entry.pack(side="left", padx=5)
        color_btn.pack(side="left", padx=5)

        font_label = tk.Label(frame, text="Font")
        font_label.pack(side="left", padx=5)
        font_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk("fonts") for f in filenames if f.endswith('.ttf')]
        font_menu = ttk.Combobox(frame, values=font_files, width="100")
        font_menu.pack(side="left", padx=5)

        self.character_entries.append((name_entry, color_entry, font_menu))

    def choose_char_color(self, entry):
        color_code = colorchooser.askcolor(title="Choose color")[1]
        if color_code:
            entry.delete(0, tk.END)
            entry.insert(0, color_code)
            entry.config(bg=color_code)

    def export_TOML(self):
        spec_toml = self.gen_toml_str()
        file_path = filedialog.asksaveasfilename(defaultextension=".toml", filetypes=[("TOML files", "*.toml")])
        if file_path:
            # Write the TOML string to the selected path
            with open(file_path, "w") as wf:
                wf.write(spec_toml)
        messagebox.showinfo("File Saved", f"TOML file saved to {file_path}")

    def load_project(self):
        print("Load Project button clicked")

    def generate_output(self):
        spec_toml = self.gen_toml_str()
        with open("./temp/spec.toml", "w") as wf:
            wf.write(spec_toml)
        os.system("Capper.exe ./temp/spec.toml -o")

    def gen_toml_str(self):
        # assemble each section of the spec.toml file
        img_path = self.image_path.get()
        bg_color = self.hex_color.get()
        # Only add image height if its set to something other than auto
        img_height_str = f"image_height = {self.img_height.get()}\n" if self.img_height.get() != "auto" else ""
        img_toml = f"[image]\nart = \"{img_path}\"\nbg_color = \"{bg_color}\"\n{img_height_str}\n"

        text_loc = self.text_loc_var.get()
        text_align = self.align_var.get()
        text_str = self.text_input.get("1.0", tk.END).strip()
        with open("./temp/text.txt", "w") as wf:
            wf.write(text_str)
        text_toml = f"[text]\ntext = \"./temp/text.txt\"\ntext_box_pos = \"{text_loc}\"\nalignment = \"{text_align}\"\n\n"

        cred_lines = self.credits_input.get("1.0", tk.END).strip().splitlines()
        cred_toml = "credits = [\n"
        for line in cred_lines:
            cred_toml += f"\"{line}\",\n"
        cred_toml += "]\n\n"

        base_name = self.base_filename.get()
        out_dir = self.output_directory.get()
        out_opt_cap = self.caption_var.get()
        out_opt_auto = self.autospec_var.get()
        out_opt_cred = self.credits_var.get()
        out_opt = []
        if (out_opt_cap):
            out_opt.append("caption")
        if (out_opt_auto):
            out_opt.append("autospec")
        if (out_opt_cred):
            out_opt.append("credits")
        # converts array into string in format of ["caption", "autospec"]
        out_opt = str(out_opt).replace("\'", "\"")
        out_toml = f"[output]\nbase_filename = \"{base_name}\"\noutput_directory = \"{out_dir}\"\noutputs = {out_opt}\n\n"

        char_toml = ""
        for i, (name_entry, color_entry, font_menu) in enumerate(self.character_entries, 1):
            char_toml += "[[characters]]\n"
            char_toml += f"name = \"{name_entry.get()}\"\n"
            char_toml += f"color = \"{color_entry.get()}\"\n"
            fixed_dir = font_menu.get().replace("\\", "/")
            char_toml += f"font = \"{fixed_dir}\"\n"
            char_toml += "\n\n"

        return img_toml + text_toml + cred_toml + out_toml + char_toml

    def get_all_values(self):
        print("Image Path:", self.image_path.get())
        print("Picked Color:", self.hex_color.get())
        print("Base Filename:", self.base_filename.get())
        print("Output Directory:", self.output_directory.get())
        print("Caption:", self.caption_var.get())
        print("Autospec:", self.autospec_var.get())

        for i, (name_entry, color_entry, font_menu) in enumerate(self.character_entries, 1):
            print(f"Character {i} Name:", name_entry.get())
            print(f"Character {i} Color:", color_entry.get())
            print(f"Character {i} Font:", font_menu.get())

        print("Text Input:", self.text_input.get("1.0", tk.END).strip())
        print("Caption Text Location:", self.align_var.get())

if __name__ == "__main__":
    app = CapperGUI()
    app.mainloop()