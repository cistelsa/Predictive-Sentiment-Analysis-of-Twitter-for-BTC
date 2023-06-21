### **Extraccion Tweets Version Alfa (v. 1.0.2):**

### **Documentación**

```python
class TweetScraper:
    def __init__(self, start_date, end_date, max_result, num_threads):
        self.start_date = start_date
        self.end_date = end_date
        self.max_result = max_result
        self.num_threads = num_threads
        self.tweets_list = []
```
- Se define la clase `TweetScraper` que representa el scraper de tweets.
- El método `__init__` se encarga de inicializar los atributos de la clase, incluyendo las fechas de inicio y fin, el número máximo de resultados a obtener y el número de hilos para la ejecución paralela. También se inicializa una lista vacía `tweets_list` para almacenar los tweets extraídos.

```python
    def clean_tweet(self, tweet):
        tweet = tweet.lower()
        tweet = re.sub(r'@[^\s]+', '', tweet)
        tweet = re.sub(r'(?<!\w)#(?!bitcoin|btc\b)\w+(?:,)?', '', tweet)
        tweet = re.sub(r'(?<!\w)\$(?!bitcoin|btc\b)\w+(?:,)?', '', tweet)
        tweet = re.sub(r'http[^\s,]+', '', tweet)
        tweet = re.sub(r'[^\w\s,$#]', '', tweet)
        tweet = re.sub(r'\s+', ' ', tweet)
        tweet = re.sub(r'^\s+|\s+$', '', tweet)

        return tweet
```
- El método `clean_tweet` se encarga de limpiar un tweet dado. Realiza una serie de transformaciones utilizando expresiones regulares:
  - Convierte el tweet a minúsculas.
  - Elimina las menciones a usuarios (@usuario).
  - Elimina los hashtags (#hashtag), excepto "#bitcoin" y "#btc".
  - Elimina los los cashtags ($cashtag), excepto "$bitcoin" y "$btc".
  - Elimina los enlaces (URLs).
  - Elimina los emoticones.
  - Elimina los espacios en blanco adicionales.
  - Elimina los espacios en blanco al inicio y al final.
  - Retorna el tweet limpio.

```python
    def scrape_tweets(self, start, end):
        sub_tweets_list = []
        tweets_ids_csv = pd.read_csv('./dataset/tweets_ids.csv')
        df_tweets_ids = pd.DataFrame(tweets_ids_csv)
        list_tweets_ids = list(df_tweets_ids['tweet_id'])
        term = '(bitcoin OR btc OR $BTC OR BTC OR BITCOIN OR $btc OR #btc OR #bitcoin) since:{} until:{} lang:en'.format(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
        print("{} in progress!".format(start.strftime('%Y-%m-%d')))
        
        existing_tweet_ids = set(list_tweets_ids)
        
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(term).get_items()):
            if i > self.max_result:
                break
            if tweet.id in existing_tweet_ids:
                continue
            try:
                cleaned_tweet = self.clean_tweet(tweet.rawContent)
                sub_tweets_list.append([tweet.id, tweet.date, cleaned_tweet, tweet

.user.id, tweet.user.username, tweet.user.displayname, tweet.user.created, tweet.user.followersCount, tweet.user.verified, tweet.user.location, tweet.likeCount, tweet.retweetCount, tweet.bookmarkCount, tweet.quoteCount, tweet.hashtags, tweet.cashtags, tweet.mentionedUsers, tweet.lang, tweet.coordinates, tweet.quotedTweet])
                existing_tweet_ids.add(tweet.id)
                
            except:
                continue
        tweets_ids = pd.DataFrame({'tweet_id': list(existing_tweet_ids)})
        tweets_ids.to_csv('./dataset/tweets_ids.csv', index=False)
        return sub_tweets_list
```
- El método `scrape_tweets` se encarga de realizar la extracción de tweets para un rango de fechas dado (start y end).
- Lee un archivo CSV llamado 'tweets_ids.csv' que contiene los IDs de los tweets existentes y los carga en un DataFrame.
- Crea una cadena de búsqueda `term` que incluye los términos de búsqueda, las fechas de inicio y fin, y el idioma.
- Inicializa un conjunto `existing_tweet_ids` con los IDs de los tweets existentes.
- Itera sobre los tweets obtenidos utilizando la biblioteca `sntwitter` y el término de búsqueda. Para cada tweet:
  - Si se ha superado el número máximo de resultados (`self.max_result`), se interrumpe la iteración.
  - Si el ID del tweet ya existe en la lista de IDs existentes, se omite y pasa al siguiente tweet.
  - Se limpia el contenido del tweet utilizando el método `clean_tweet`.
  - Se agrega una lista con los atributos relevantes del tweet (ID, fecha, texto limpio, etc.) a `sub_tweets_list`.
  - Se agrega el ID del tweet a la lista de IDs existentes.
- Se crea un nuevo DataFrame `tweets_ids` con los IDs de los tweets existentes.
- Se guarda este DataFrame en el archivo 'tweets_ids.csv'.
- Retorna `sub_tweets_list`, que contiene los tweets extraídos.

```python
    def scrape_parallel(self):
        date_range = pd.date_range(start=self.start_date, end=self.end_date, freq='1D')

        files_csv = glob.glob('./dataset/*.csv')
        filename_list_csv = [os.path.basename(file) for file in files_csv]
        
        output_filename_base = f'tweets_{self.start_date.strftime("%Y-%m-%d")}_{self.end_date.strftime("%Y-%m-%d")}'
        output_filename = output_filename_base + '.csv'

        if output_filename in filename_list_csv:
            
            incremental_number = 1
            while f"{output_filename_base}_{incremental_number}.csv" in filename_list_csv:
                incremental_number += 1
            
            
            new_output_filename = f"{output_filename_base}_{incremental_number}.csv"
        else:
           
            new_output_filename = output_filename_base + ".csv"
```
- El método `scrape_parallel` se encarga de realizar la extracción paralela de tweets utilizando múltiples hilos.
- Crea un rango de fechas `date_range` utilizando la biblioteca `pandas`.
- Obtiene una lista de archivos CSV en el directorio actual y extrae los nombres de archivo sin la ruta completa.
- Define el nombre base del archivo de salida en función de

 las fechas de inicio y fin.
- Verifica si el nombre de archivo de salida ya existe en la lista de archivos CSV.
  - Si existe, extrae el número incremental del archivo existente y construye un nuevo nombre de archivo con el número incremental.
  - Si no existe, utiliza el nombre base de archivo de salida tal cual.
- El resultado final es el nombre de archivo de salida, almacenado en `new_output_filename`.

```python
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = []
            for i in range(len(date_range) - 1):
                start = date_range[i]
                end = date_range[i+1]
                futures.append(executor.submit(self.scrape_tweets, start, end))
            
            for future in futures:
                sub_tweets_list = future.result()
                self.tweets_list.extend(sub_tweets_list)
```
- Se utiliza un `ThreadPoolExecutor` para ejecutar la extracción de tweets en paralelo.
- Se crean tareas `futures` para cada rango de fechas, donde cada tarea ejecuta el método `scrape_tweets` con los parámetros correspondientes.
- Se espera a que todas las tareas se completen y se obtienen los resultados.
- Los resultados (sub_tweets_list) se agregan a la lista `self.tweets_list`.

```python
        tweets2_df = pd.DataFrame(self.tweets_list, columns=['tweet_id', 'datetime', 'text', 'user_id', 'screen_name', 'full_name', 'user_created', 'followers_count', 'user_verified', 'user_location', 'likes', 'retweet_count', 'bookmark_count', 'quote_count', 'hashtags', 'cashtags', 'mentions', 'language', 'coodinates', 'quoted_tweet_id'])
        tweets2_df.to_csv('./dataset/' + new_output_filename, index=False, sep='|')
        print(f"Output file generated: {new_output_filename}")
```
- Se crea un nuevo DataFrame `tweets2_df` a partir de `self.tweets_list`, con las columnas correspondientes.
- Se guarda este DataFrame en un archivo CSV con el nombre `new_output_filename`, utilizando el separador '|' y sin incluir el índice.
- Se imprime un mensaje indicando que se ha generado el archivo de salida.

```python
# Decorador para medir el tiempo de ejecución
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print("Execution time: {}".format(execution_time))
    return wrapper


@measure_execution_time
def main():
    start_date = datetime(2023, 4, 7)
    end_date = datetime(2023, 4, 9)
    max_result = 50000
    num_threads = 10
    
    scraper = TweetScraper(start_date, end_date, max_result, num_threads)
    scraper.scrape_parallel()
```
- Se define un decorador `measure_execution_time` que mide el tiempo de ejecución de una función.
- Se define una función `main` que representa el punto de entrada del programa.
- Se establecen los valores de las variables para las fechas de inicio y fin, el número máximo de resultados y el número de hilos.
- Se crea una instancia de `TweetScraper` con los valores establecidos.
- Se llama al método `scrape_parallel` de la instancia de `TweetScraper` para iniciar la extracción paralela de tweets.
- La función `main` está decorada con `measure_execution_time`, por lo que se imprimirá el tiempo de ejecución total al finalizar la función.

### **Resumen**

Esta app tiene un código que define una clase `TweetScraper` que se encarga de extraer tweets de Twitter en un rango de fechas dado. El método `scrape_parallel` permite la extracción paralela utilizando múltiples hilos. Los tweets extraídos se limpian y se guardan en un archivo CSV. La función `main` establece los parámetros de configuración y ejecuta el proceso de extracción de tweets.