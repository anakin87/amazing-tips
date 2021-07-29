from polyglot.detect import Detector
  

def is_ocr_good(text_filepath, language, min_confidence):
    detector = Detector
    with open(text_filepath, 'r') as fin:
        text = fin.read()
    # corrected text to prevent polyglot errors    
    corr_text = ''.join(x for x in text if x.isprintable())

    try:
        detection = detector(corr_text)
        good_ocr = detection.language.name==language \
            and detection.language.confidence>=min_confidence
    except:
        good_ocr = False

    return good_ocr   