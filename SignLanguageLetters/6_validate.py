import re
import inspect
from ultralytics import YOLO

_showRegex = re.compile(r'\bshow\s*\(\s*(.*)\s*\)')

def show(var):
	varName = ''
	for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
		m = _showRegex.search(line)
		if m:
			varName = m.group(1)
			break
	print('{0} = {1}'.format(varName, var))


def val(model_pt):
    show(model_pt)
    model = YOLO(model_pt)
    metrics = model.val()
    show(metrics.box.map)
    show(metrics.box.map50)
    show(metrics.box.map75)
    show(metrics.box.maps)
    print()

if __name__ == "__main__":
    val("../runs/detect/train/weights/best.pt")
    val("../runs/detect/train/weights/last.pt")