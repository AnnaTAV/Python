import fileio
import UI

data = fileio.read_data("data.csv")
UI.menu(data)