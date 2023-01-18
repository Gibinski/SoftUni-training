def loading_bar(load):
    loading_bar_ = ("%" * (load // 10)) + ("." * (10 - load // 10))
    if load < 100:
        print(f"{load}% [{loading_bar_}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{loading_bar_}]")

loading = int(input())
loading_bar(loading)