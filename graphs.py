def annual_transit_bar(SPREADSHEET_NAME, WORKSHEET_NAME, CREDENTIALS_FILE, limited_1, limited_2, limited_total):
    import plotly.express as px
    import plotly.graph_objects as go
    from pull_annual_transit_data import pull_sheet_data
    
    transit_totals_full_df = pull_sheet_data(SPREADSHEET_NAME, WORKSHEET_NAME, CREDENTIALS_FILE)

    transit_totals_df = transit_totals_full_df[['EG_morning', 'EG_afternoon', 'EG Loop Supplementals','EG_Total', 'BT_morning', 
    'BT_afternoon','WG Loop Supplementals', 'BT_Total', 'UC Total', 'Daily Total', 'NL Total', 'NC Total', 'Night Total', 'Bike Shuttle Total',
    limited_total, 'WSC Shuttle', 'SVC Shuttle', 'Total']]

    # print(transit_totals_df)

    colors = px.colors.qualitative.Plotly 

    fig2 = go.Figure(data=[
        go.Bar(name="EG_Total",x=transit_totals_df.index, y=transit_totals_df['EG_Total'], marker_color=colors[0]),
        go.Bar(name="BT_Total",x=transit_totals_df.index, y=transit_totals_df['BT_Total'], marker_color=colors[1]),
        go.Bar(name="Night Total",x=transit_totals_df.index, y=transit_totals_df['Night Total'], marker_color=colors[2]),
        go.Bar(name="Upper Campus Total",x=transit_totals_df.index, y=transit_totals_df['UC Total'], marker_color=colors[3]),
        go.Bar(name=f"{limited_total}",x=transit_totals_df.index, y=transit_totals_df[limited_total], marker_color=colors[4]),
        go.Bar(name="Bike Shuttle Total",x=transit_totals_df.index, y=transit_totals_df['Bike Shuttle Total'], marker_color=colors[6]),
        go.Bar(name="SVC Shuttle",x=transit_totals_df.index, y=transit_totals_df['SVC Shuttle'], marker_color=colors[7]),
        go.Bar(name="WSC Shuttle",x=transit_totals_df.index, y=transit_totals_df['WSC Shuttle'], marker_color=colors[8]),
        
        ])
    fig2.update_layout(barmode='stack', title='Stacked Bar Chart', yaxis=dict(range=[0, 200000], autorange=False))


    column_sums = transit_totals_df[[
        'EG_Total', 'BT_Total', 'Night Total', 'UC Total', 
        limited_total, 'Bike Shuttle Total', 'SVC Shuttle', 'WSC Shuttle'
    ]].sum()

    fig_pie = go.Figure(data=[go.Pie(
        labels=column_sums.index, 
        values=column_sums.values,
        marker=dict(colors=colors),
        hole=.3  # Optional: makes it a Donut chart
    )])

    fig_pie.update_layout(title_text='Total Annual Transit Distribution')
    
    
    return fig2, fig_pie
