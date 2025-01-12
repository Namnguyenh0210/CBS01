import queue

class MP3Player:
    def __init__(self):
        self.song_queue = queue.Queue()  # Hàng đợi bài hát
        self.current_song = None  # Bài hát hiện đang chơi

    def add_song(self, song):
        """Thêm bài hát vào danh sách chờ."""
        self.song_queue.put(song)
        print(f"Đã thêm bài hát '{song}' vào danh sách chờ.")

    def play_next_song(self):
        """Chơi bài hát tiếp theo trong danh sách chờ."""
        if not self.song_queue.empty():  # Kiểm tra danh sách chờ có bài hát
            self.current_song = self.song_queue.get()  # Lấy bài hát ra khỏi hàng đợi
            print(f"Đang chơi bài hát: '{self.current_song}'")
        else:
            print("Không có bài hát nào trong danh sách chờ.")

    def skip_song(self):
        """Bỏ qua bài hát hiện tại."""
        if self.current_song is None:
            print("Không có bài hát nào đang chơi.")
        else:
            print(f"Bài hát '{self.current_song}' đã bị bỏ qua.")
            self.current_song = None
            self.play_next_song()

# Sử dụng lớp MP3Player
mp3_player = MP3Player()

# Thêm bài hát
mp3_player.add_song("Bài hát 1")
mp3_player.add_song("Bài hát 2")
mp3_player.add_song("Bài hát 3")

mp3_player.play_next_song()  
mp3_player.skip_song()  
mp3_player.skip_song()  
mp3_player.skip_song()  
