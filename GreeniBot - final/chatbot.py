import customtkinter as ctk
import tkinter as tk 
from PIL import Image, ImageTk 
import tkinter.font as tkfont
import json
import os
import uuid
import time
import re 
import random

KNOWLEDGE_BASE = {
    "bagaimana kendaraan bermotor menyebabkan emisi karbon": "Kendaraan bermotor membakar bahan bakar fosil (bensin/diesel), melepaskan gas buang seperti karbon dioksida (CO2) dan gas rumah kaca lainnya yang berkontribusi pada pemanasan global.",
    "berapa kontribusi sektor transportasi terhadap emisi nasional": "Di Indonesia, sektor transportasi merupakan salah satu penyumbang emisi karbon terbesar. Menurut data, kontribusinya bisa mencapai sekitar 20-25% dari total emisi nasional, terutama dari penggunaan kendaraan pribadi.",
    "bagaimana cara mengurangi jejak karbon perjalanan saya": "Untuk mengurangi jejak karbon perjalanan Anda, pertimbangkan untuk beralih ke transportasi umum (bus, kereta), bersepeda, berjalan kaki, atau menggunakan kendaraan listrik/hybrid jika memungkinkan. Menggabungkan perjalanan dan mengemudi secara efisien juga membantu.",
    "apa dampak jika saya beralih dari motor ke transportasi publik selama setahun": "Jika Anda beralih dari motor ke transportasi publik selama setahun, Anda dapat mengurangi emisi CO2 secara signifikan, menghemat biaya bahan bakar, mengurangi kemacetan, dan berkontribusi pada udara yang lebih bersih. Estimasi pengurangan emisi bisa mencapai ratusan kilogram CO2 per tahun, tergantung jarak tempuh.",
    "apa itu emisi karbon": "Emisi karbon adalah pelepasan gas karbon ke atmosfer bumi, terutama karbon dioksida (CO2), yang sebagian besar dihasilkan dari pembakaran bahan bakar fosil oleh aktivitas manusia dan menjadi penyebab utama perubahan iklim.",
    "dampak emisi karbon bagi lingkungan": "Dampak emisi karbon antara lain pemanasan global, perubahan iklim ekstrem (banjir, kekeringan), kenaikan permukaan air laut, kerusakan ekosistem laut (pemutihan karang), dan masalah kesehatan akibat polusi udara.",
    "tips transportasi berkelanjutan": "Tips transportasi berkelanjutan meliputi: gunakan angkutan umum, bersepeda atau berjalan kaki untuk jarak dekat, pertimbangkan kendaraan listrik, manfaatkan carpooling, dan rawat kendaraan Anda agar efisien bahan bakar.",
    "definisi perubahan iklim": "Perubahan iklim adalah pergeseran signifikan dan jangka panjang dalam pola cuaca global atau regional, terutama disebabkan oleh peningkatan konsentrasi gas rumah kaca di atmosfer akibat aktivitas manusia.",
    "apa sumber utama emisi karbon": "Sumber utama emisi karbon meliputi pembakaran bahan bakar fosil untuk energi listrik dan transportasi, deforestasi, aktivitas industri, dan pertanian intensif yang menghasilkan gas metana (CH4) dan dinitrogen oksida (N2O).",
    "apa hubungan deforestasi dengan emisi karbon": "Deforestasi mengurangi kemampuan bumi menyerap karbon dioksida karena berkurangnya pepohonan. Selain itu, proses penebangan dan pembakaran hutan melepaskan karbon yang tersimpan di biomassa pohon ke atmosfer.",
    "bagaimana energi terbarukan dapat mengurangi emisi karbon": "Energi terbarukan seperti tenaga surya, angin, hidro, dan biomassa menghasilkan listrik tanpa membakar bahan bakar fosil. Dengan menggantikan sumber energi berbasis fosil, emisi CO2 dapat dikurangi secara drastis.",
    "apa dampak emisi karbon terhadap kesehatan manusia": "Emisi karbon sering kali disertai polutan lain seperti partikulat (PM2.5) dan nitrogen oksida yang dapat menyebabkan gangguan pernapasan, penyakit jantung, dan memperburuk kondisi kronis seperti asma.",
    "apa itu jejak karbon": "Jejak karbon adalah total emisi gas rumah kaca yang dihasilkan langsung maupun tidak langsung oleh aktivitas individu, organisasi, atau produk, biasanya dinyatakan dalam satuan kilogram atau ton CO2 ekuivalen.",
    "bagaimana cara menghitung jejak karbon pribadi": "Jejak karbon pribadi dihitung dari aktivitas sehari-hari seperti penggunaan kendaraan, konsumsi listrik, pola makan, dan perjalanan udara. Banyak kalkulator daring yang bisa memperkirakan emisi total berdasarkan data kegiatan Anda.",
    "apa itu netral karbon": "Netral karbon (carbon neutrality) berarti kondisi ketika jumlah emisi karbon yang dikeluarkan setara dengan jumlah yang diserap kembali melalui upaya seperti reboisasi, efisiensi energi, atau kompensasi karbon.",
    "contoh kebijakan pengurangan emisi karbon": "Beberapa kebijakan yang diterapkan negara untuk mengurangi emisi karbon antara lain penerapan pajak karbon, perdagangan emisi (carbon trading), subsidi energi terbarukan, dan larangan pembakaran hutan.",
    "apa peran individu dalam mitigasi emisi karbon": "Individu dapat berperan penting dengan mengadopsi gaya hidup berkelanjutan seperti menghemat energi, memilih transportasi ramah lingkungan, mengurangi konsumsi daging, dan mendukung produk atau perusahaan yang ramah lingkungan.",
    "perbedaan CO2 dan gas rumah kaca lainnya": "CO2 adalah gas rumah kaca paling umum dari pembakaran bahan bakar. Namun ada juga gas lain seperti metana (CH4), dinitrogen oksida (N2O), dan gas fluorinated yang memiliki efek pemanasan lebih besar meski dalam jumlah lebih sedikit.",
    "bagaimana sektor industri menyumbang emisi karbon": "Sektor industri menghasilkan emisi karbon melalui proses produksi, penggunaan energi fosil untuk mesin, dan reaksi kimia (seperti pembuatan semen dan baja) yang melepaskan CO2 ke atmosfer.",
    "apa hubungan konsumsi energi listrik dengan emisi karbon": "Sebagian besar listrik di Indonesia masih dihasilkan dari pembangkit berbahan batu bara atau gas. Semakin tinggi konsumsi listrik, semakin besar pula emisi karbon jika energi tersebut belum berasal dari sumber terbarukan.",
    "apa itu penyerapan karbon (carbon capture)": "Penyerapan karbon (Carbon Capture, Utilization, and Storage/CCUS) adalah teknologi yang menangkap CO2 dari sumber emisi besar (pembangkit listrik, pabrik), kemudian disimpan secara permanen di bawah tanah atau digunakan untuk tujuan lain.",
    "bagaimana pertanian dapat berkontribusi pada emisi karbon": "Pertanian dapat menyumbang emisi melalui penggunaan pupuk nitrogen (menghasilkan N2O), pencernaan ternak (menghasilkan metana dari sapi), dan perubahan penggunaan lahan seperti pembukaan lahan gambut.",
    "bagaimana kota-kota dapat mengurangi emisi karbon": "Kota-kota dapat mengurangi emisi dengan mempromosikan transportasi publik, mengembangkan infrastruktur hijau, meningkatkan efisiensi energi bangunan, mengelola limbah dengan baik, dan menggunakan sumber energi terbarukan.",
    "apa itu kredit karbon": "Kredit karbon adalah izin yang memungkinkan pemegang untuk mengeluarkan satu ton karbon dioksida. Ini dapat diperdagangkan, memungkinkan perusahaan untuk membeli 'hak' untuk beremisi atau menjual 'penghematan' emisi mereka.",
    "apa hubungan antara konsumsi daging dan emisi karbon": "Produksi daging, terutama daging merah, membutuhkan lahan, air, dan pakan yang besar. Ternak juga menghasilkan metana. Konsumsi daging yang lebih rendah dapat mengurangi jejak karbon pribadi secara signifikan.",
    "bagaimana teknologi cerdas dapat membantu mengurangi emisi": "Teknologi cerdas seperti smart grid, sensor IoT untuk efisiensi energi di bangunan, optimasi rute transportasi, dan analisis data untuk memprediksi konsumsi energi dapat membantu mengurangi emisi.",
    "apa itu transisi energi": "Transisi energi adalah pergeseran global dari sistem energi berbasis bahan bakar fosil ke sistem energi berkelanjutan yang mengandalkan sumber energi terbarukan dan teknologi rendah karbon.",
    "dampak emisi karbon pada biota laut": "Peningkatan CO2 di atmosfer menyebabkan lautan menyerap lebih banyak CO2, yang mengakibatkan pengasaman laut. Ini merusak kerang-kerangan, terumbu karang, dan ekosistem laut lainnya.",
    "apa itu karbon biru (blue carbon)": "Karbon biru adalah karbon yang disimpan di ekosistem pesisir dan laut seperti hutan bakau, padang lamun, dan rawa payau. Ekosistem ini sangat efektif dalam menyerap dan menyimpan karbon.",
    "bagaimana reboisasi dan aforestasi mengurangi emisi": "Reboisasi (penanaman kembali hutan) dan aforestasi (penanaman hutan di lahan yang belum pernah berhutan) membantu menyerap CO2 dari atmosfer melalui fotosintesis, menyimpannya di biomassa pohon dan tanah.",
    "apa itu mitigasi perubahan iklim": "Mitigasi perubahan iklim adalah tindakan untuk mengurangi emisi gas rumah kaca atau meningkatkan penyerapan gas rumah kaca, untuk memperlambat atau menghentikan pemanasan global.",
    "bagaimana pembangunan berkelanjutan berkaitan dengan emisi karbon": "Pembangunan berkelanjutan berupaya memenuhi kebutuhan generasi sekarang tanpa mengorbankan kemampuan generasi mendatang. Ini mencakup pengurangan emisi karbon melalui praktik ekonomi dan sosial yang bertanggung jawab lingkungan.",
    "apa itu EBT (Energi Baru Terbarukan)": "EBT adalah singkatan dari Energi Baru Terbarukan, yaitu sumber energi yang berasal dari proses alam yang berkelanjutan, seperti tenaga surya, angin, air (hidro), panas bumi, biomassa, dan ombak. Pengembangannya sangat penting untuk mengurangi emisi karbon.",
    "apa peran bank dalam mendukung pengurangan emisi karbon": "Bank dapat mendukung pengurangan emisi karbon dengan memberikan pinjaman untuk proyek energi terbarukan, mendanai inisiatif hijau, menawarkan produk keuangan berkelanjutan, dan mengadopsi kebijakan investasi yang bertanggung jawab lingkungan."
}


ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue")

class SophisticatedChatbotApp:
    CHAT_FILE = "chat_history.json"
    KB = KNOWLEDGE_BASE

    STOP_WORDS = {

    'apa', 'itu', 'adalah', 'dari', 'dan', 'di', 'untuk', 'dengan', 'saya', 'ke', 'bagaimana',
    'yang', 'bisa', 'dapat', 'akan', 'atau', 'pada', 'juga', 'peran', 'dalam', 'hubungan',
    'antara', 'sektor', 'dampak', 'jika', 'cara', 'contoh', 'saja', 'lainnya', 'perbedaan',
    'berapa', 'terhadap', 'bagi', 'tips', 'memengaruhi', 'motor', 'mobil', 'publik', 'selama', 'setahun',
    'beralih', 'mengurangi', 'saya', 'milik', 'pribadi', 'kita', 'emisi', 'karbon', 'biota', 'laut',
    'kebijakan', 'individu', 'pembangunan', 'berkelanjutan', 'umum', 'transportasi',
    'adalahnya', 'seperti', 'karena', 'oleh', 'agar', 'disebabkan', 'menjadi', 'sebagai', 
    'pada', 'tentang', 'disebut', 'dimana', 'mengapa', 'misalnya', 'dapatkah', 'apakah', 'yakni',
    'termasuk', 'melalui', 'terutama', 'contohnya', 'disebabkan', 'dihasilkan', 'aktivitas',
    'menghasilkan', 'penggunaan', 'penghasil', 'terjadi', 'tersebut', 'dalamnya', 'maupun', 
    'lain', 'beberapa', 'adanya', 'adapun', 'karakteristik', 'mempengaruhi',
    'gas', 'rumah', 'kaca', 'perubahan', 'iklim', 'pengurangan', 'peningkatan', 'penyumbang',
    'kontribusi', 'nasional', 'penggunaan', 'penghasil', 'penyebab', 'penyimpanan', 'penyerapan',
    'pembakaran', 'pembangkit', 'penerapan', 'produksi', 'penghasil', 'penggunaan', 'proses',
    'pembuatan', 'pemakaian', 'aktivitas', 'penggunaan', 'peningkatan', 'pengurangan',
    'besar', 'tinggi', 'utama', 'utama', 'signifikan', 'berasal', 'berkontribusi', 'berhubungan',
    'penting', 'umumnya', 'khususnya', 'global', 'nasional', 'lokal', 'lain',
    'sebuah', 'suatu', 'tersebut', 'lebih', 'dari', 'yang', 'oleh', 'juga', 'ini', 'itu', 'dan',
    'ke', 'di', 'pada', 'untuk', 'karena', 'agar', 'hingga', 'sehingga', 'maka', 'bahwa'
}

    GREETINGS = [
    "Halo! Saya siap membantu Anda mengenai emisi karbon dan transportasi berkelanjutan. Apa yang ingin Anda ketahui hari ini?",
    "Selamat datang! Silakan tanyakan apa pun tentang jejak karbon atau isu iklim. Saya punya banyak informasi untuk dibagikan!",
    "Hai! Senang bertemu Anda. Mari kita bahas bagaimana kita bisa menjaga planet ini. Pertanyaan apa yang ada di benak Anda?",
    "Salam! Saya adalah chatbot pengetahuan tentang isu lingkungan. Bagaimana saya bisa melayani Anda?",
    "Apa kabar? Saya adalah basis pengetahuan yang hidup. Tanyakan saja tentang emisi, transportasi, atau kebijakan hijau.",
    "Hai! Terima kasih sudah mampir. Mau ngobrol soal emisi karbon, energi bersih, atau transportasi ramah lingkungan?",
    "Halo! Yuk, kita bahas cara-cara sederhana untuk bantu kurangi emisi karbon di sekitar kita.",
    "Selamat datang kembali! Ada topik lingkungan tertentu yang ingin Anda pelajari hari ini?",
    "Hai, senang Anda datang! Saya bisa bantu menjelaskan soal perubahan iklim, energi terbarukan, atau kebijakan hijau.",
    "Halo! Bagaimana harimu? Mari kita lihat bersama bagaimana tindakan kecil bisa berdampak besar bagi bumi.",
    "Halo! 🌎 Saya di sini untuk bantu Anda memahami dunia energi bersih dan keberlanjutan.",
    "Selamat datang! Siap untuk berbincang soal masa depan hijau dan solusi rendah karbon?",
    "Hai! Kalau Anda penasaran tentang emisi karbon atau cara hidup ramah lingkungan, Anda datang ke tempat yang tepat!",
    "Halo! Saya suka berbicara tentang lingkungan — mau mulai dari transportasi, energi, atau gaya hidup hijau?",
    "Hai, teman bumi! 🌱 Mari kita cari tahu bagaimana kita bisa menjaga planet ini tetap sehat bersama.",
    "Selamat datang di zona hijau! Siap belajar hal baru tentang iklim dan emisi karbon hari ini?",
    "Halo! Apa kabar? Saya bisa bantu menjelaskan topik apa saja seputar karbon, energi, dan keberlanjutan.",
    "Hai! Mari kita buat percakapan ini bermanfaat bagi bumi. Apa yang ingin Anda tanyakan duluan?",
    "Halo! Saya senang bisa bantu Anda memahami dunia karbon dan lingkungan dengan cara yang sederhana.",
    "Hai! 🌤️ Mau tahu cara kecil yang bisa Anda lakukan untuk bantu bumi hari ini?",
    "Halo! Yuk, mulai percakapan ramah lingkungan kita. Topik apa yang menarik buat Anda?"
]

    GOODBYES = [
    "Sampai jumpa lagi! Jangan ragu untuk kembali jika ada pertanyaan lain tentang keberlanjutan.",
    "Terima kasih sudah berbincang. Mari terus berjuang untuk lingkungan yang lebih baik!",
    "Senang membantu Anda. Semoga perjalanan Anda selalu ramah lingkungan!",
    "Sampai jumpa! Ingat, setiap tindakan kecil Anda berarti besar untuk planet ini.",
    "Jaga diri, dan semoga hari Anda menyenangkan! Selamat tinggal.",
    "Terima kasih atas diskusinya! Saya menunggu pertanyaan Anda berikutnya.",
    "Sampai bertemu lagi! Semoga hari Anda penuh energi positif dan hijau 🌱",
    "Terima kasih sudah peduli pada bumi. Sampai jumpa di percakapan berikutnya!",
    "Senang bisa berbagi ilmu hari ini. Jangan lupa istirahat dan hirup udara segar!",
    "Terima kasih! Teruslah jadi bagian dari solusi untuk masa depan yang lebih bersih 💚",
    "Selamat tinggal! Semoga langkah kecil Anda hari ini membawa dampak besar bagi bumi.",
    "Sampai jumpa! Tetap semangat menjaga lingkungan, ya!",
    "Terima kasih atas obrolannya! Dunia butuh lebih banyak orang seperti Anda 🌎",
    "Senang sekali bisa membantu. Semoga pengetahuan ini bermanfaat bagi Anda!",
    "Baiklah, saya pamit dulu. Sampai jumpa di percakapan ramah lingkungan berikutnya!",
    "Terima kasih sudah meluangkan waktu. Yuk, terus dukung gaya hidup hijau!",
    "Sampai jumpa, teman bumi! 🌿 Jangan berhenti peduli pada planet kita.",
    "Terima kasih, semoga hari Anda cerah dan penuh semangat hijau!",
    "Selamat tinggal! Ingat, perubahan besar selalu dimulai dari langkah kecil.",
    "Sampai nanti! Kalau ada yang ingin Anda tanyakan soal iklim, saya selalu siap membantu.",
    "Terima kasih atas perhatian Anda untuk bumi. Mari terus berbuat baik untuk alam."
]

    def __init__(self, master):
        self.master = master
        master.title("GreeniBot")
        master.geometry("1000x700") 
        
      
        self.chats = {}
        self.current_chat_id = None
        self.chat_history_buttons = {}
        self._load_chats_from_file() 
        

        self.MAIN_BG = "#202124" 
        self.SIDEBAR_COLOR = "#292A2D" 
        self.INPUT_COLOR = "#3C4043" 
        self.TEXT_COLOR_LIGHT = "#F1F3F4" 
        self.TEXT_COLOR_MUTED = "#C0C0C0" 
        self.ACCENT_COLOR = "#4285F4"
        self.ACCENT_HOVER = "#2A6AD4" 
        self.ACCENT_TEXT = "#98D1FF"
        
        master.configure(fg_color=self.MAIN_BG)

      
        self.font_family = "Inter" 
        
        self.app_font = ctk.CTkFont(family=self.font_family, size=18) 
        self.sidebar_font = ctk.CTkFont(family=self.font_family, size=15) 
        self.title_font = ctk.CTkFont(family=self.font_family, size=23, weight="bold")
        self.welcome_font = ctk.CTkFont(family=self.font_family, size=32, weight="bold") 
        self.input_font = ctk.CTkFont(family=self.font_family, size=18)


        self._load_icons()
        

        self.context_menu = tk.Menu(master, tearoff=0, bg=self.SIDEBAR_COLOR, fg=self.TEXT_COLOR_LIGHT, 
                                     activebackground=self.ACCENT_COLOR, activeforeground="white")


        self.main_frame = ctk.CTkFrame(master, fg_color=self.MAIN_BG)
        self.main_frame.pack(fill=tk.BOTH, expand=True)


        self.sidebar_frame = ctk.CTkFrame(self.main_frame, fg_color=self.SIDEBAR_COLOR, width=250, corner_radius=0)
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0,1))
        self.sidebar_frame.pack_propagate(False) 


        self.chat_area_frame = ctk.CTkFrame(self.main_frame, fg_color=self.MAIN_BG)
        self.chat_area_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


        self._setup_sidebar()
        self._setup_chat_area()
        
        self.user_input.focus_set()
        

        if not self.chats:
            self.new_chat()
        else:

            sorted_chats = sorted(self.chats.items(), key=lambda item: item[1].get('timestamp', 0), reverse=True)
            self.load_chat(sorted_chats[0][0])


    def _clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text) 
        text = re.sub(r'[^\x00-\x7F]+', '', text)
        words = text.split()
        return set(word for word in words if word not in self.STOP_WORDS and len(word) > 2)

    def _get_kb_response(self, user_query):
        query_words = self._clean_text(user_query)
        best_match_key = None
        max_overlap = 0

        if not query_words:
            return None

        for kb_key in self.KB.keys():
            kb_words = self._clean_text(kb_key)
            
            overlap = len(query_words.intersection(kb_words))
            
            if overlap > max_overlap:
                max_overlap = overlap
                best_match_key = kb_key

        if max_overlap >= 1: 
            return self.KB[best_match_key]
        else:
            return None

    def _is_greeting(self, query):
        q = query.lower().strip()
        return any(g in q for g in [

        "halo", "hai", "hei", "hey", "helo", "heloo", "halloo", "selamat pagi",
        "selamat siang", "selamat sore", "selamat malam", "apa kabar",
        "assalamualaikum", "salam", "selamat datang",
        "pagi", "siang", "sore", "malam",
        
        "hello", "hi", "hey there", "good morning", "good afternoon",
        "good evening", "how are you", "what’s up", "what up", "yo",
        "hiya", "sup", "howdy", "morning", "evening", "greetings",

        "heyy", "heyyy", "yo bro", "wassup", "sup bro", "hey bot",
        "hey buddy", "hi there", "hey man", "hey dude", "hii", "helloo",
        "long time no see", "nice to meet you", "how’s it going",
        "how r u", "gimana kabarnya", "apa kabar bot"])

    def _is_goodbye(self, query):
        q = query.lower().strip()
        return any(g in q for g in [
        "terima kasih", "makasih", "thanks ya", "makasih ya", "sampai jumpa",
        "dadah", "dada", "selamat tinggal", "cukup", "itu saja", "sudah cukup",
        "oke makasih", "baik terima kasih", "terima kasih banyak", "ok thanks",
        "terima kasih ya", "mantap makasih", "makasih banget", "see you nanti",
        "sampai ketemu", "ok dah", "bye", "bai", "udah ya", "cukup ya",

        "thank you", "thanks", "thanks a lot", "thanks so much", "thank u",
        "thank u so much", "bye", "goodbye", "see you", "see ya",
        "see you later", "later", "take care", "catch you later",
        "talk to you later", "peace out", "bye bye", "ciao", "adios",
        "farewell", "see you soon", "later bro", "im done", "i’m good now",

        "ty", "thx", "thx bro", "ok bye", "okey bye", "bye bot",
        "gtg", "gonna go", "brb", "see u", "ok done", "that’s all",
        "done for now", "ok cool thanks", "alright thanks", "thanks dude"
        ])

    def _get_bot_response(self, user_query):

        
        if self._is_greeting(user_query):
            return random.choice(self.GREETINGS)

        if self._is_goodbye(user_query):
            return random.choice(self.GOODBYES)
        kb_answer = self._get_kb_response(user_query)
        
        if kb_answer:
            return kb_answer
        else:
            return "Maaf, saya hanya bisa menjawab pertanyaan seputar emisi karbon dan transportasi berkelanjutan yang ada dalam basis pengetahuan saya. Silakan coba pertanyaan yang lebih spesifik, atau periksa kembali kata kunci Anda."


    def _load_chats_from_file(self):

        if os.path.exists(self.CHAT_FILE):
            try:
                with open(self.CHAT_FILE, 'r') as f:
                    self.chats = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error reading chat file: {e}. Starting fresh.")
                self.chats = {}
        else:
            self.chats = {}

    def _save_chats_to_file(self):

        try:
            with open(self.CHAT_FILE, 'w') as f:
                json.dump(self.chats, f, indent=4)
        except IOError as e:
            print(f"Error writing chat file: {e}")


    def _load_icons(self):

        try:
            icon_size_sm = (16, 16)
            icon_size_md = (20, 20)

            self.gemini_logo = None
            self.new_chat_icon = None
            self.user_avatar = None
            self.plus_icon = None
            self.square_icon = None

        except Exception as e:
            print(f"Icon loading failed (using fallbacks): {e}")


    def _setup_sidebar(self):

        logo_frame = ctk.CTkFrame(self.sidebar_frame, fg_color=self.SIDEBAR_COLOR, height=50)
        logo_frame.pack(fill=tk.X, pady=(0, 5), padx=10)
        
        logo_content = " ▨ GreeniBot" 
        if self.gemini_logo:
            ctk.CTkLabel(logo_frame, image=self.gemini_logo, text="", fg_color=self.SIDEBAR_COLOR).pack(side=tk.LEFT, padx=(0, 5), pady=10)
            ctk.CTkLabel(logo_frame, text="GreeniBot", font=self.title_font, text_color=self.TEXT_COLOR_LIGHT).pack(side=tk.LEFT, padx=0, pady=10)
        else:
            ctk.CTkLabel(logo_frame, text=logo_content, font=self.title_font, text_color=self.TEXT_COLOR_LIGHT).pack(side=tk.LEFT, padx=5, pady=10)


        new_chat_button = ctk.CTkButton(
            self.sidebar_frame,
            text=" New chat",
            image=self.new_chat_icon if self.new_chat_icon else None,
            compound=tk.LEFT,
            command=self.new_chat,
            font=self.sidebar_font,
            fg_color=self.ACCENT_COLOR, 
            hover_color=self.ACCENT_HOVER,
            text_color="white",
            corner_radius=8,
            height=36
        )
        new_chat_button.pack(fill=tk.X, padx=10, pady=5)


        ctk.CTkLabel(self.sidebar_frame, text="Chats", font=ctk.CTkFont(family=self.font_family, size=12, weight="bold"), 
                      text_color=self.TEXT_COLOR_MUTED, anchor="w").pack(fill=tk.X, pady=(10,2), padx=10)
        

        self.scrollable_chat_frame = ctk.CTkScrollableFrame(self.sidebar_frame, fg_color=self.SIDEBAR_COLOR, corner_radius=0)
        self.scrollable_chat_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        

        self._update_sidebar() 


        user_info_frame = ctk.CTkFrame(self.sidebar_frame, fg_color=self.SIDEBAR_COLOR, corner_radius=0)
        user_info_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        ctk.CTkFrame(user_info_frame, fg_color="#303134", height=1, corner_radius=0).pack(fill=tk.X, padx=10, pady=5)

        user_profile_frame = ctk.CTkFrame(user_info_frame, fg_color=self.SIDEBAR_COLOR)
        user_profile_frame.pack(fill=tk.X, padx=10)

        if self.user_avatar:
            ctk.CTkLabel(user_profile_frame, image=self.user_avatar, text="", fg_color=self.SIDEBAR_COLOR).pack(side=tk.LEFT, padx=(0, 5))
        else:
            ctk.CTkLabel(user_profile_frame, text="👤", font=(self.font_family, 16), text_color=self.TEXT_COLOR_LIGHT).pack(side=tk.LEFT, padx=(0, 5))
        
        ctk.CTkLabel(user_profile_frame, text="User", font=self.sidebar_font, text_color=self.TEXT_COLOR_LIGHT, justify=tk.LEFT).pack(side=tk.LEFT, anchor="w", pady=10)

    def _update_sidebar(self):
        for widget in self.scrollable_chat_frame.winfo_children():
            widget.destroy()
        self.chat_history_buttons = {}

        sorted_chats = sorted(self.chats.items(), key=lambda item: item[1].get('timestamp', 0), reverse=True)

        for chat_id, chat_data in sorted_chats:
            title = chat_data.get('title', 'New Chat')
            
            display_title = title if len(title) < 30 else title[:27] + '...'

            button_color = self.ACCENT_COLOR if chat_id == self.current_chat_id else "transparent"
            hover_color = "#3A3B3D" if chat_id != self.current_chat_id else self.ACCENT_HOVER

            chat_item_button = ctk.CTkButton(
                self.scrollable_chat_frame, 
                text=display_title, 
                font=self.sidebar_font, 
                fg_color=button_color, 
                hover_color=hover_color,
                text_color=self.TEXT_COLOR_LIGHT,
                anchor="w",
                command=lambda i=chat_id: self.load_chat(i),
                corner_radius=8,
                height=32
            )
            chat_item_button.pack(fill=tk.X, padx=10, pady=2)
            
            chat_item_button.bind("<Button-3>", lambda event, i=chat_id: self._show_context_menu(event, i))

            self.chat_history_buttons[chat_id] = chat_item_button
            

    def _show_context_menu(self, event, chat_id):
        self.context_menu.delete(0, tk.END)
        
        self.context_menu.add_command(label="Rename Chat", command=lambda: self._prompt_rename(chat_id))
        self.context_menu.add_command(label="Delete Chat", command=lambda: self._prompt_delete_confirmation(chat_id))
        
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
            

    def _prompt_rename(self, chat_id):
        if chat_id not in self.chats: return

        rename_dialog = ctk.CTkToplevel(self.master)
        rename_dialog.title("Rename Chat")
        rename_dialog.geometry("350x150")
        rename_dialog.transient(self.master)
        rename_dialog.grab_set()
        rename_dialog.lift()

        current_title = self.chats[chat_id]['title']
        
        ctk.CTkLabel(rename_dialog, text="Enter new chat title:", font=self.sidebar_font).pack(pady=10, padx=20)
        
        entry = ctk.CTkEntry(rename_dialog, width=300, font=self.sidebar_font)
        entry.insert(0, current_title)
        entry.pack(pady=5, padx=20)
        entry.focus_set()

        def save_rename():
            new_title = entry.get().strip()
            if new_title:
                self.rename_chat(chat_id, new_title)
            rename_dialog.destroy()

        def on_return(event):
            save_rename()
        
        entry.bind("<Return>", on_return)

        button_frame = ctk.CTkFrame(rename_dialog, fg_color="transparent")
        button_frame.pack(pady=10)
        
        ctk.CTkButton(button_frame, text="Cancel", command=rename_dialog.destroy, fg_color="gray", hover_color="darkgray", font=self.sidebar_font).pack(side=tk.LEFT, padx=10)
        ctk.CTkButton(button_frame, text="Rename", command=save_rename, font=self.sidebar_font, fg_color=self.ACCENT_COLOR).pack(side=tk.LEFT, padx=10)

        self.master.update_idletasks()
        x = self.master.winfo_x() + (self.master.winfo_width() - 350) // 2
        y = self.master.winfo_y() + (self.master.winfo_height() - 150) // 2
        rename_dialog.geometry(f"+{x}+{y}")
        
    def rename_chat(self, chat_id, new_title):
        if chat_id in self.chats:
            self.chats[chat_id]['title'] = new_title
            
            if chat_id == self.current_chat_id:
                self.chat_title_label.configure(text=new_title)
                
            self._update_sidebar()
            self._save_chats_to_file()
            

    def _prompt_delete_confirmation(self, chat_id):
        if chat_id not in self.chats: return

        confirm_dialog = ctk.CTkToplevel(self.master)
        confirm_dialog.title("Confirm Deletion")
        confirm_dialog.geometry("350x150")
        confirm_dialog.transient(self.master)
        confirm_dialog.grab_set()
        confirm_dialog.lift()
        
        title_to_delete = self.chats[chat_id]['title']
        
        ctk.CTkLabel(confirm_dialog, text=f"Are you sure you want to delete:", font=self.sidebar_font).pack(pady=(15, 0), padx=20)
        ctk.CTkLabel(confirm_dialog, text=f"'{title_to_delete}'?", font=ctk.CTkFont(family=self.font_family, size=14, weight="bold")).pack(pady=5, padx=20)


        def perform_delete():
            self.delete_chat(chat_id)
            confirm_dialog.destroy()

        button_frame = ctk.CTkFrame(confirm_dialog, fg_color="transparent")
        button_frame.pack(pady=10)
        
        ctk.CTkButton(button_frame, text="Cancel", command=confirm_dialog.destroy, fg_color="gray", hover_color="darkgray", font=self.sidebar_font).pack(side=tk.LEFT, padx=10)
        ctk.CTkButton(button_frame, text="Delete", command=perform_delete, fg_color="#CC0000", hover_color="#990000", font=self.sidebar_font).pack(side=tk.LEFT, padx=10)
        
        self.master.update_idletasks()
        x = self.master.winfo_x() + (self.master.winfo_width() - 350) // 2
        y = self.master.winfo_y() + (self.master.winfo_height() - 150) // 2
        confirm_dialog.geometry(f"+{x}+{y}")


    def delete_chat(self, chat_id):
        if chat_id in self.chats:
            del self.chats[chat_id]
            self._save_chats_to_file()
            
            if chat_id == self.current_chat_id:
                self.current_chat_id = None
                
                if self.chats:
                    sorted_chats = sorted(self.chats.items(), key=lambda item: item[1].get('timestamp', 0), reverse=True)
                    self.load_chat(sorted_chats[0][0])
                else:
                    self.new_chat()
            
            self._update_sidebar()


    def _setup_chat_area(self):

        top_content_frame = ctk.CTkFrame(self.chat_area_frame, fg_color=self.SIDEBAR_COLOR, height=50, corner_radius=0) 
        top_content_frame.pack(fill=tk.X)
        top_content_frame.pack_propagate(False)
        
        self.chat_title_label = ctk.CTkLabel(top_content_frame, text="GreeniBot", font=self.title_font, text_color=self.TEXT_COLOR_LIGHT)
        self.chat_title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        

        content_grid_frame = ctk.CTkFrame(self.chat_area_frame, fg_color=self.MAIN_BG)
        content_grid_frame.pack(fill=tk.BOTH, expand=True)
        
        content_grid_frame.grid_rowconfigure(0, weight=1) 
        content_grid_frame.grid_rowconfigure(1, weight=0) 
        content_grid_frame.grid_columnconfigure(0, weight=1)


        self.welcome_label = ctk.CTkLabel(
            content_grid_frame,
            text="Halo!\n\nMulailah percakapan dengan mengetik pertanyaan Anda di bawah.", 
            font=ctk.CTkFont(family=self.font_family, size=28, weight="bold"),
            text_color=self.TEXT_COLOR_MUTED,
            fg_color=self.MAIN_BG
        )
        self.welcome_label.grid(row=0, column=0, sticky="nsew") 


        self.chat_history = ctk.CTkTextbox(
            content_grid_frame,
            wrap=tk.WORD,
            font=self.app_font, 
            fg_color=self.MAIN_BG, 
            text_color=self.TEXT_COLOR_LIGHT,
            border_width=0,
            corner_radius=0,
            padx=100, 
            pady=30,
            activate_scrollbars=True
        )
        self.chat_history.configure(state="disabled") 


        self.chat_history.tag_config('prefix', foreground=self.TEXT_COLOR_MUTED) 
        self.chat_history.tag_config('user', foreground=self.ACCENT_TEXT) 
        self.chat_history.tag_config('bot', foreground=self.TEXT_COLOR_LIGHT)
        self.chat_history.tag_config('loading', foreground='#FFD700')


        input_bar_container = ctk.CTkFrame(
            content_grid_frame,
            fg_color=self.INPUT_COLOR, 
            corner_radius=24,
            height=60 
        )
        input_bar_container.grid(row=1, column=0, sticky="ew", padx=100, pady=(0, 20)) 
        input_bar_container.grid_propagate(False) 
        
 
        if self.plus_icon:
            ctk.CTkLabel(input_bar_container, image=self.plus_icon, text="", fg_color=self.INPUT_COLOR).pack(side=tk.LEFT, padx=(15, 5))
        else:
            ctk.CTkLabel(input_bar_container, text="➕", font=(self.font_family, 16), text_color=self.TEXT_COLOR_MUTED).pack(side=tk.LEFT, padx=(15, 5))

 
        

        self.send_button = ctk.CTkButton(
            input_bar_container,
            text="Send", 
            command=self.send_message,
            width=35,
            height=35,
            fg_color=self.ACCENT_COLOR,
            hover_color=self.ACCENT_HOVER,
            corner_radius=20
        )
        self.send_button.pack(side=tk.RIGHT, padx=10)
        
        if self.square_icon:
            ctk.CTkLabel(
            input_bar_container,
            text="",
            fg_color=self.INPUT_COLOR
        ).pack(side=tk.RIGHT, padx=5)
        else:
            ctk.CTkLabel(
                input_bar_container,
                text="◻",
                font=(self.font_family, 16),
                text_color=self.TEXT_COLOR_MUTED
            ).pack(side=tk.RIGHT, padx=5)
 
        self.user_input = ctk.CTkEntry(
            input_bar_container,
            font=self.input_font,
            placeholder_text="Masukkan pertanyaan Anda...",
            border_width=0,
            fg_color=self.INPUT_COLOR, 
            text_color=self.TEXT_COLOR_LIGHT,
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5, padx=(10, 10))
        self.user_input.bind("<Return>", lambda event: self.send_message())
        
        self.welcome_label.tkraise()

    def load_chat(self, chat_id):
        if chat_id not in self.chats:
            return

        self.current_chat_id = chat_id
        chat_data = self.chats[chat_id]
        self.chat_title_label.configure(text=chat_data.get('title', 'GrreeniBot'))

        self.chat_history.configure(state="normal")
        self.chat_history.delete(1.0, tk.END)
        self.welcome_label.grid_forget()
        self.chat_history.grid(row=0, column=0, sticky="nsew") 

        for message in chat_data.get('messages', []):
            sender = message.get('sender')
            text = message.get('text')
            tag = 'user' if sender == 'User' else 'bot'
            self._display_message_content(sender, text, tag)
            
        self.chat_history.configure(state="disabled")
        self.chat_history.yview(tk.END)
        
        self._update_sidebar() 

    def new_chat(self):
        """Creates a new chat session."""
        new_id = str(uuid.uuid4())
        initial_title = time.strftime("New Chat (%H:%M)")
        
        self.chats[new_id] = {
            'title': initial_title,
            'messages': [],
            'timestamp': time.time()
        }
        
        self.current_chat_id = new_id
        
        self._update_sidebar()
        
      
        self.chat_history.configure(state="normal")
        self.chat_history.delete(1.0, tk.END)
        self.chat_history.configure(state="disabled")
   
        
        self.chat_history.grid_forget()
        self.welcome_label.grid(row=0, column=0, sticky="nsew")
        self.chat_title_label.configure(text="GreeniBot")
        
        self.user_input.focus_set()
        self._save_chats_to_file()

    def _display_message_content(self, sender, message, tag):
        prefix = "Anda: " if sender == 'User' else "GreeniBot: "
        self.chat_history.insert(tk.END, "\n")
        self.chat_history.insert(tk.END, prefix, 'prefix') 
        self.chat_history.insert(tk.END, f"{message}\n", tag) 

    def display_message(self, sender, message, tag):
        if self.welcome_label.winfo_ismapped():
            self.welcome_label.grid_forget()
            self.chat_history.grid(row=0, column=0, sticky="nsew") 

        self.chat_history.configure(state="normal")
        
        if sender == 'User' and self.current_chat_id in self.chats and not self.chats[self.current_chat_id]['messages']:
            title_text = message.split('\n')[0] 
            display_title = title_text if len(title_text) < 50 else title_text[:47] + '...'
            self.chats[self.current_chat_id]['title'] = display_title
            self.chat_title_label.configure(text=display_title)
            self._update_sidebar()
            
        self._display_message_content(sender, message, tag)
            
        if self.current_chat_id in self.chats:
            self.chats[self.current_chat_id]['messages'].append({
                'sender': sender,
                'text': message
            })
            self.chats[self.current_chat_id]['timestamp'] = time.time()
            self._save_chats_to_file()

        self.chat_history.yview(tk.END)
        self.chat_history.configure(state="disabled")


    def send_message(self):
        user_query = self.user_input.get().strip()
        if not user_query or not self.current_chat_id:
            return

        self.user_input.delete(0, tk.END)
        
        self.display_message("User", user_query, 'user')
        
        bot_response = self._get_bot_response(user_query)

        self.display_message("System", bot_response, 'bot')
        
        self.user_input.focus_set()


if __name__ == '__main__':
    root = ctk.CTk()
    app = SophisticatedChatbotApp(root)
    root.mainloop()
