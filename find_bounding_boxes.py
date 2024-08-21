import cv2


def main():
    img = cv2.imread(
        "underwater_mosaic_database/ophiuroidea/masks_and_overlays/B6_0040_30s/mask-Ophiuroidea.png"
    )
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ok, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w * h > 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Gray", img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
