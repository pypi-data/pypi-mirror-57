This Dashboard uses Yahoo ticker symbols for identifying financial securities and fetches the available historical data from Yahoo servers. The downloaded data is returned in the form of a data object wrapping a Pandas DataFrame (Fields: Open, Close, High, Low, Adj_Close, Volume). The downloaded data is stored locally in a series of SQL databases for allowing offline work with known data. When working online with new data flowing in, the Dashboard constantly compares the inbound data with the local copy and keeps updating the SQL databases appending the new points.

The returned data object upon data request offers as well some simple tools/functionalities for requesting filtered data, as well as for rendering different types of financial plots (close, ohlc, candlestick).

The module offers as well a separate basic service for searching and filtering Yahoo ticker symbols by ticker symbol, security name, exchage, type of security, and more. The database of available Yahoo ticker symbols in which the search is carried out gets updated periodically with information of securities in most exchanges worldwide.


