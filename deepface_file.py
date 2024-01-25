from deepface import DeepFace

def deepface_main(pFilepath):
    result = DeepFace.analyze(img_path = pFilepath,
        actions = ['emotion']
    )
    return result[0]["dominant_emotion"]

