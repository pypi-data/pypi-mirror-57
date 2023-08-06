import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="path to video file")
parser.add_argument("--frameskip", help="A positive integer N (default: 30). Keywords will be collected every Nth frame.", type=int, default=30)
parser.add_argument("--showvideo", dest="showvideo", action="store_true", default=False)
parser.add_argument("--progressbar", dest="progressbar", action="store_true", default=False)
parser.add_argument("--probability-threshold", type=float, default=0.2,
        help="A number between 0 and 1. Will only generate keywords classified above the threshold")
parser.add_argument("--occurence-threshold", type=int, default=1,
        help="A positive integer. Will only generate keywords occuring more times than the threshold.")

args = parser.parse_args()

if args.file:
    from vidtag import video_tagger


def main():
    tags = video_tagger(args.file,
                        frameskip=args.frameskip,
                        show_video=args.showvideo,
                        progress_bar=args.progressbar,
                        probability_threshold=args.probability_threshold,
                        occurence_threshold=args.occurence_threshold)

    print(" ".join(tags))

if __name__ == "__main__":
    main()
