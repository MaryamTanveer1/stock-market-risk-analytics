CREATE EXTERNAL TABLE IF NOT EXISTS stock_data_processed (
    date string,
    close double,
    daily_return double,
    `50_day_ma` double,
    `200_day_ma` double
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
    'serialization.format' = ',',
    'field.delim' = ','
)
LOCATION 's3://stock-market-data-demo-maryam-gen/processed/'
TBLPROPERTIES (
    'has_encrypted_data'='false',
    'skip.header.line.count'='1'
);

SELECT * FROM stock_data_processed LIMIT 10;