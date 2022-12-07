from math import ceil


class PhotoAlbum:
    PHOTOS_ON_PAGE = 4
    
    
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]


    @classmethod
    def from_photos_count(cls, photos_count: int): 
        return cls(ceil(photos_count / PhotoAlbum.PHOTOS_ON_PAGE))


    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < PhotoAlbum.PHOTOS_ON_PAGE:
                self.photos[page].append(label)
                
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
    
        return "No more free slots"


    def display(self):
        dashes = "-" * 11
        result = [dashes]
        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(dashes)
        
        return "\n".join(result)


# Test Code
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())



