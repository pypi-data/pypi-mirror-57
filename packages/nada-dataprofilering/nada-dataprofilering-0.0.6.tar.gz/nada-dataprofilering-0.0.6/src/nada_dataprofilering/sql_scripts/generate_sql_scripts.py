from string import Template


def generate_table_columns(schema, table):
    sql_string = "select column_name from all_col_comments where owner = '$SCHEMA' and table_name = '$TABLE'"
    sql_template = Template(sql_string)
    sql_template_filled = sql_template.substitute(SCHEMA=schema, TABLE=table)

    return sql_template_filled


def generate_standard_column_metrics(schema, table, column):
    sql_string = """with 
                    a as (select    '$SCHEMA' as schema, 
                                    '$TABLE' as table_name, 
                                    '$COLUMN' as column_name,
                                    count($COLUMN) as num_rows,
                                    count(distinct $COLUMN) as num_distinct,
                                    count(case when $COLUMN is null then 1 end) as num_nulls
                                    
                                    from $SCHEMA.$TABLE),
                                    
                    b as (select    column_name, 
                                    data_type 
                                    from all_tab_cols where owner = '$SCHEMA' and table_name = '$TABLE' and column_name = '$COLUMN')
                    
                    select a.schema, 
                            a.table_name, 
                            a.column_name, 
                            a.num_rows, 
                            a.num_distinct,
                            a.num_nulls,
                            b.data_type
                            from a
                    inner join b on
                            a.column_name = b.column_name
                            """
    sql_template = Template(sql_string)
    sql_template_filled = sql_template.substitute(SCHEMA=schema, TABLE=table, COLUMN=column)

    return sql_template_filled


def generate_numeric_metrics(schema, table, column):
    sql_string = """select 
                        MIN($COLUMN) as min,
                        MAX($COLUMN) as max,
                        MEDIAN($COLUMN) as median,
                        AVG($COLUMN) as mean,
                        VARIANCE($COLUMN) as variance,
                        SQRT(VARIANCE($COLUMN)) as standard_deviation
                        
                    from $SCHEMA.$TABLE """

    sql_template = Template(sql_string)
    sql_template_filled = sql_template.substitute(SCHEMA=schema, TABLE=table, COLUMN=column)

    return sql_template_filled


def generate_datetime_metrics(schema, table, column):
    sql_string = """select 
                        MIN($COLUMN) as first_date,
                        MAX($COLUMN) as last_date
                        MAX($COLUMN) - MIN($COLUMN))as NUM_DAYS,
                        MONTHS_BETWEEN( MAX($COLUMN), MIN($COLUMN)) as NUM_MONTHS,
                        (MONTHS_BETWEEN( MAX($COLUMN), MIN($COLUMN)))/12 as NUM_YEARS,
                        COUNT(distinct $COLUMN) as NUM_DATES
                    
                    from $SCHEMA.$TABLE """

    sql_template = Template(sql_string)
    sql_template_filled = sql_template.substitute(SCHEMA=schema, TABLE=table, COLUMN=column)

    return sql_template_filled


def generate_datetime_compare_metrics(schema, table, start_column, end_column):
    sql_string = """select 
                        count($END_COLUMN - $START_COLUMN) as NUM_END_BEFORE_START 
                    from $SCHEMA.TABLE where $END_COLUMN - $ START_COLUMN <0 """

    sql_template = Template(sql_string)
    sql_template_filled = sql_template.substitute(SCHEMA=schema, TABLE=table, START_COLUMN=start_column,
                                                  END_COLUMN=end_column)

    return sql_template_filled


def generate_varchar2_metrics(schema, table, column):
    sql_string = """select
                        MIN(LENGTH($COLUMN)) as MIN_CHAR,
                        MAX(LENGTH($COLUMN) as MAX_CHAR,
                        AVG(LENGTH($COLUMN)) as AVG_CHAR,
                        COUNT(distinct $COLUMN) as DISTINCT_COUNT,
                        COUNT(distinct $COLUMN)/COUNT($COLUMN)*100 as DISTINCT_PER_COLUMN
                    from $SCHEMA.$TABLE"""

    sql_template = Template(sql_string)
    sql_template_filled = sql_template.substitute(SCHEMA=schema, TABLE=table, COLUMN= column)

    return sql_template_filled


def generate_hist(schema, table, column):
    sql_string = """select  
                        count($COLUMN),
                        $COLUMN
                    from $SCHEMA.$TABLE
                    group by $COLUMN
                    order by $COLUMN desc"""

    sql_template = Template(sql_string)
    sql_template_filled = sql_template.substitute(SCHEMA=schema, TABLE=table, COLUMN=column)

    return sql_template_filled

