# Audio Annotation Helper - For AI Data Labeling
def create_annotation():
    print("--- Audio Annotation Tool ---")
    audio_file = input("Enter audio file name (ex: sample.mp3): ")
    
    annotations = []
    while True:
        start = input("Enter start time (ex: 00:02) or type 'q' to finish: ")
        if start.lower() == 'q':
            break
        end = input("Enter end time (ex: 00:05): ")
        label = input("Enter label (Speaker 1 / Music / Background Noise): ")
        
        annotations.append(f"{start} - {end} : {label}")
        print(f"Added -> {start} - {end} : {label}")

    # Save to txt file
    with open("annotations.txt", "w") as f:
        f.write(f"Audio File: {audio_file}\n")
        f.write("------------------------\n")
        for line in annotations:
            f.write(line + "\n")
    
    print("\nDone! Annotation saved to annotations.txt")
    print("This format is used for AI model training.")

create_annotation()
