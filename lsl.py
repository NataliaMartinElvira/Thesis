from pylsl import resolve_stream

def list_streams():
    streams = resolve_stream()
    if not streams:
        print("No LSL streams found.")
    else:
        print(f"Found {len(streams)} LSL streams:")
        for stream in streams:
            print(f"Name: {stream.name()}, Type: {stream.type()}")

if __name__ == "__main__":
    list_streams()
