import folium

def crear_mapa_satelital(
  lat,
  lon,
  zoom=12,
  mostrar_marcador=True,
  archivo_html="mapa_satelital.html",
  archivo_png="mapa_satelital.png",
  ancho=2560,
  alto=1440,
):
  """
  Crea un mapa con vista satelital y lo guarda como HTML y PNG.
  
  :param lat: Latitud del centro del mapa
  :param lon: Longitud del centro del mapa
  :param zoom: Nivel de zoom inicial
  :param mostrar_marcador: Si es False, no dibuja el pin en el centro
  :param archivo_html: Nombre del archivo HTML de salida
  :param archivo_png: Nombre del archivo PNG de salida
  :param ancho: Ancho del mapa (px), usado para mejorar la calidad del PNG
  :param alto: Alto del mapa (px), usado para mejorar la calidad del PNG
  """
  # Crear mapa base sin tiles por defecto
  mapa = folium.Map(location=[lat, lon], zoom_start=zoom, tiles=None, width=ancho, height=alto)

  # Agregar capa satelital (Esri World Imagery)
  folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Tiles © Esri",
    name="Esri Satélite",
    overlay=False,
    control=True
  ).add_to(mapa)

  # Control para activar/desactivar capas
  folium.LayerControl().add_to(mapa)

  # Exportar PNG en alta resolución.
  # Requiere selenium y un webdriver disponible en el sistema.
  try:
    png_data = mapa._to_png(delay=5)
    with open(archivo_png, "wb") as archivo:
      archivo.write(png_data)
    print(f"Mapa guardado en PNG (alta calidad): {archivo_png}")
  except Exception as error:
    print("No se pudo exportar a PNG automáticamente.")
    print("Instala 'selenium' y un webdriver (Chrome/Firefox) para habilitar la captura.")
    print(f"Detalle: {error}")

if __name__ == "__main__":
  # Ciudad de mexico
  latitud = 19.4326
  longitud = -99.1332
  crear_mapa_satelital(
    latitud,
    longitud,
    zoom=30,
    mostrar_marcador=False,
    archivo_html="cdmx_satelital.html",
    archivo_png="cdmx_satelital.png",
    ancho=2560,
    alto=1440,
  )