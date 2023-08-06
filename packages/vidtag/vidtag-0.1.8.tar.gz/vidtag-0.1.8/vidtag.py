import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
import tensorflow as tf
import cv2
from tqdm import tqdm

#Load image classifier
classifier = tf.keras.applications.vgg16.VGG16()


def video_tagger(path, frameskip=30, show_video=False,
                 probability_threshold=0.2, occurence_threshold=1,
                 progress_bar=False):
    """
    Produces keywords for a video file.

    Parameters:
        path: Path to video file.

    Optional parameters:
        frameskip: A positive integer N.
                   Keywords will be collected every Nth frame.
        show_video: True or False. If True, the video will play
                    during keyword capture.
        probability_threshold: A number between 0 and 1. Will only
                               generate keywords classified above the
                               threshold.
        occurence_threshold: A positive integer. Will only generate
                             keywords occuring more times than
                             the threshold.
        progress_bar: True or False. If true, displays a progress bar.

    Returns:
        A list of keywords.

    """

    if frameskip < 1:
        raise ValueError('Frameskip must be positive.')

    if not os.path.isfile(path):
        raise FileNotFoundError('No such file.')

    #Create list of tags by running every Nth frame through image classifier
    tags = []
    vid = cv2.VideoCapture(path)
    num_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    if show_video:
        cv2.namedWindow('window',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('window',600,600)

    if progress_bar:
        t = tqdm(total=num_frames)

    for k in range(num_frames-1):
        ret, frame = vid.read()
        if not ret:
            if progress_bar:
                t.close()
            break

        if k%frameskip == 0:

            if show_video:
                cv2.imshow('window',frame)

            frame = np.expand_dims(frame, axis=0)
            frame = tf.keras.applications.vgg16.preprocess_input(frame)
            frame = tf.image.resize(frame,(224,224))
            preds = tf.keras.applications.vgg16.decode_predictions(
                        classifier.predict(frame), top=5)[0]
            preds = [ p[1] for p in preds if p[2] > probability_threshold]

            tags += preds

        if cv2.waitKey(1) & 0xFF == ord('q'):
            if progress_bar:
                t.close()
            break

        if progress_bar:
            t.update(1)

    if progress_bar:
        t.close()

    tags = sorted(tags)
    tags_set = set(tags)
    tags_set = sorted(tags_set)
    counts = [tags.count(w) for w in tags_set]
    popular_tags_zip = sorted(zip(counts,tags_set), reverse=True)
    popular_tags_set = [tag[1] for tag in popular_tags_zip if tag[0] > occurence_threshold]
    popular_tags_count = [tag[0] for tag in popular_tags_zip if tag[0] > occurence_threshold]
    vid.release()

    if show_video:
        cv2.destroyWindow('window')

    return popular_tags_set
