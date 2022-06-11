import cv2 as cv

def draw(path):
    draw = False
    ix, iy = -1, -1

    def rectangle_draw(event, x, y, flag_val, par):
        global draw, ix, iy

        if event == cv.EVENT_LBUTTONDOWN:
            draw = True
            ix, iy = x, y
        elif event == cv.EVENT_LBUTTONUP:
            draw = False
            cv.rectangle(image_window, (ix, iy), (x, y), (255, 0, 0), -1)

    image_window = cv.imread(path)
    image_window = cv.resize(image_window, (612, 792))
    cv.namedWindow(winname='image_window')
    cv.setMouseCallback('image_window', rectangle_draw)

    while True:
        cv.imshow("image_window", image_window)
        cv.imwrite(path, image_window)
        if cv.waitKey(1) & 0xFF == 27:
            break

    cv.destroyAllWindows()


def highlight(path):
    draw = False
    ix, iy = -1, -1

    def rectangle_draw(event, x, y, flag_val, par):
        global draw, ix, iy

        if event == cv.EVENT_LBUTTONDOWN:
            draw = True
            ix, iy = x, y
        elif event == cv.EVENT_LBUTTONUP:
            draw = False
            cv.rectangle(image_window, (ix, iy), (x, y), (255, 0, 0), -1)
            cv.addWeighted(image_window, 0.8, overlay, 1 - 0.2, 0, image_window)

    image_window = cv.imread(path)
    image_window = cv.resize(image_window, (612, 792))
    overlay = image_window.copy()
    cv.namedWindow(winname='image_window')
    cv.setMouseCallback('image_window', rectangle_draw)

    while True:
        cv.imshow("image_window", image_window)
        cv.imwrite(path, image_window)
        if cv.waitKey(1) & 0xFF == 27:
            break

    cv.destroyAllWindows()


def draw_marker(path):
    image = cv.imread(path)
    image = cv.resize(image, (612, 792))
    overlay = image.copy()
    cv.rectangle(image, (50, 50), (33, 0), (0, 0, 255), 3)
    cv.imshow("marked Image", image)
    cv.waitKey(0)

