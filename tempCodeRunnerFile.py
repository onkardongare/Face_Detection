                    cv2.putText(img,f"{int(detection.score[0] * 100)} %", (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)   
