from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.lib import colors
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.barcharts import VerticalBarChart
from energyusage.RAPLFile import RAPLFile


import energyusage.convert as convert

year = "2016"

styles = getSampleStyleSheet()
TitleStyle = ParagraphStyle(name='Normal', fontSize=16, alignment= TA_CENTER, fontName="Times-Bold")
SubtitleStyle = ParagraphStyle(name='Normal',fontSize=12, alignment= TA_CENTER, fontName="Times-Roman")
# MonospacedSubtitleStyle = ParagraphStyle(name='Normal',fontSize=12, alignment= TA_CENTER, fontName="Courier")
HeaderStyle = ParagraphStyle(name='Normal',fontSize=16)
SubheaderStyle = ParagraphStyle(name='Normal', fontName="Times-Roman")
DescriptorStyle = ParagraphStyle(name='Normal',fontSize=14, alignment= TA_CENTER)
BodyTextStyle = styles["BodyText"]
Elements = []


def bold(text):
    return "<b>"+text+"</b>"

def title(text, style=TitleStyle, klass=Paragraph, sep=0.3):
    """ Creates title of report """
    t = klass(bold(text), style)
    Elements.append(t)

def subtitle(text, style=SubtitleStyle, klass=Paragraph, sep=0.1, spaceBefore=True, spaceAfter = True):
    """ Creates descriptor text for a (sub)section; sp adds space before text """
    s = Spacer(0, 1.5*sep*inch)
    if spaceBefore:
        Elements.append(s)
    d = klass(text, style)
    Elements.append(d)
    if spaceAfter:
        Elements.append(s)



def readings_and_mix_table(reading_data, mix_data, breakdown, state_emission, location):
    '''
    Creates 2 tables that are then embedded as the columns of 1 bigger table
    '''
    no_rows = 1
    no_cols = 1
    col_size = 4.5

    readings_table = Table(reading_data, no_cols*[col_size/2*inch], 5*[0.25*inch] + [0.3*inch], hAlign="LEFT")
    readings_table.setStyle(TableStyle([('FONT', (0,0), (-1,-1), "Times-Roman"),
                                         ('FONT', (0,0), (-1,0), "Times-Bold"),
                                         ('FONTSIZE', (0,0), (-1,-1), 12),
                                         ('FONTSIZE', (0,0), (-1,0), 13),
                                         ('ALIGN', (0,0), (0,-1), "RIGHT"),
                                         ('VALIGN', (-1,-1), (-1,-1), "TOP")]))


    d = Drawing(100, 100)
    pc = Pie()

    data = []
    if state_emission:
        data = ["Coal", "Oil", "Natural Gas", "Low Carbon"]
    else:
        data = ["Coal", "Petroleum", "Natural Gas", "Low Carbon"]

    for i in range(4):
        data[i] += ": " + str(round(breakdown[i], 1)) + "%"

    pc.x = 45
    pc.y = 0
    pc.width = 55
    pc.height = 55
    pc.data = breakdown[:4]
    pc.slices[0].fillColor = colors.Color(202.0/255, 0.0/255, 32.0/255)
    pc.slices[1].fillColor = colors.Color(244.0/255, 165.0/255, 130.0/255)
    pc.slices[2].fillColor = colors.Color(5.0/255, 113.0/255, 176.0/255)
    pc.slices[3].fillColor = colors.Color(146.0/255, 197.0/255, 222.0/255)
    pc.labels = data
    pc.slices.strokeWidth=0.5
    pc.sideLabels = True
    d.add(pc)


    mix_data = [['Energy Mix Data'], [d], ['Location: ' + location]]
    mix_table = Table(mix_data, no_cols*[col_size/2*inch], [.25*inch, 1*inch, .3*inch], hAlign="RIGHT")
    mix_table.setStyle(TableStyle([('FONT', (0,0), (-1,-1), "Times-Roman"),
                                   ('FONT', (0,0), (0,0), "Times-Bold"),
                                   ('FONTSIZE', (0,0), (0,0), 13),
                                   ('FONTSIZE', (-1,-1), (-1,-1), 12),
                                   ('ALIGN', (0,0), (0,0), "LEFT")]))


    table_data = [(readings_table, mix_table)]
    t = Table(table_data, [4.25*inch, 3*inch], hAlign='CENTER')
    t.setStyle(TableStyle([('VALIGN', (-1,-1), (-1,-1), "TOP")]))
    Elements.append(t)


def kwh_and_emissions_table(data):

    s = Spacer(9*inch, .2*inch)
    Elements.append(s)

    no_rows = 1
    no_cols = 2
    col_size = 2

    t = Table(data, [2.75*inch, 2.15*inch],[.25*inch, .29*inch], hAlign="CENTER")
    t.setStyle([('FONT',(0,0),(-1,-1),"Times-Roman"),
                ('FONT',(0,0),(0,-1),"Times-Bold"),
                ('FONTSIZE', (0,0), (-1,-1), 12),
                ('ALIGN', (0,0), (0,-1), "RIGHT"),
                ('ALIGN',(1,1),(1,-1), "LEFT"),
                ('BOX', (0,0), (-1,-1), 1, colors.black),
                ('VALIGN', (0,0), (-1,-1), "TOP")])
    Elements.append(t)


def equivs_and_emission_equivs(equivs_data, emissions_data):
    '''
    Creates a table with 2 columns, each with their own embedded table
    The embedded tables contain 2 vertically-stacked tables, one for the header
    and the other one for the actual data in order to have better alignment

    The first row of the 2nd vertically-stacked table is smaller than the rest in
    order to remove the extra space and make these tables look cohesive with the
    energy usage readings and energy mix tables

    Setup:
    * Table(data[array of arrays, one for each row], [column widths], [row heights])
    * Spacer(width, height)


    '''
    s = Spacer(9*inch, .2*inch)
    Elements.append(s)

    no_rows = 1
    no_cols = 1
    col_size = 4.5

    equivs_header_data = [["Assumed Carbon Equivalencies"]]

    # Table(data)
    equivs_header_table = Table(equivs_header_data, [3*inch], [.25*inch])
    equivs_header_table.setStyle(TableStyle([('FONT',(0,0),(0,-1),"Times-Bold"),
                                             ('FONTSIZE', (0,0), (-1,-1), 13)]))


    equivs_data_table = Table(equivs_data, [1*inch, 2*inch], [0.17*inch, 0.25*inch, 0.25*inch, 0.25*inch],hAlign="LEFT")
    equivs_data_table.setStyle(TableStyle([('FONT', (0,0), (-1,-1), "Times-Roman"),
                                         ('FONTSIZE', (0,0), (-1,-1), 12),
                                         ('ALIGN', (0,0), (0,-1), "RIGHT"),
                                         ('VALIGN', (-1,-1), (-1,-1), "TOP")]))

    t1_data = [[equivs_header_table],[equivs_data_table]]

    t1 = Table(t1_data, [3*inch])

    emission_equiv_para = Paragraph('<font face="times" size=13><strong>CO<sub rise = -10 size = 8>2</sub>' +
    '  Emissions Equivalents</strong></font>', style = styles["Normal"])
    emissions_header_data = [[emission_equiv_para]]
    emissions_header_table = Table(emissions_header_data, [3*inch], [.25*inch])
    emissions_header_table.setStyle(TableStyle([('FONT',(0,0),(0,-1),"Times-Bold"),
                                             ('FONTSIZE', (0,0), (-1,-1), 13)]))


    emissions_data_table = Table(emissions_data, [2.1*inch, 1.5*inch], [0.17*inch, 0.25*inch, 0.25*inch],hAlign="LEFT")
    emissions_data_table.setStyle(TableStyle([('FONT', (0,0), (-1,-1), "Times-Roman"),
                                         ('FONTSIZE', (0,0), (-1,-1), 12),
                                         ('ALIGN', (0,0), (0,-1), "RIGHT"),
                                         ('VALIGN', (-1,-1), (-1,-1), "TOP")]))

    t2_data = [[emissions_header_table],[emissions_data_table]]

    t2 = Table(t2_data, [3*inch])


    table_data = [(t1, t2)]
    t = Table(table_data, [4.25*inch, 3*inch], hAlign='CENTER')
    t.setStyle(TableStyle([('VALIGN', (-1,-1), (-1,-1), "TOP")]))
    Elements.append(t)


def comparison_graphs(comparison_values, location, emission):
    s = Spacer(9*inch, .2*inch)
    Elements.append(s)
    
    labels = []
    data = []
    comparison_values.append([location, emission])
    comparison_values.sort(key = lambda x: x[1])
    for pair in comparison_values:
        labels.append(pair[0])
        data.append(pair[1])
    location_index = labels.index(location)
    data = [data]
    '''
    Trial and error on making this centered and looking good; seems like if
    just inserted into the table, it moves all the way to the right; hence
    the x = -150 to center it, and -120 to move it downwards so it doesn't
    overlap with the top of the graph
    '''
    drawing = Drawing(0, 0)
    bc = VerticalBarChart()
    bc.x = -150
    bc.y = -120
    bc.height = 125
    bc.width = 300
    bc.data = data
    bc.strokeColor = colors.black
    bc.valueAxis.valueMin = 0
    bc.valueAxis.valueMax = data[0][-1] + data[0][-1] *.1
    #bc.valueAxis.valueStep = 10
    bc.categoryAxis.labels.boxAnchor = 'ne'
    bc.categoryAxis.labels.dx = 8
    bc.categoryAxis.labels.dy = -2
    bc.categoryAxis.labels.angle = 30
    bc.categoryAxis.categoryNames = labels
    for i in range(len(labels)):
        bc.bars[(0, i)].fillColor = colors.Color(166.0/255, 189.0/255, 219.0/255)
    bc.bars[(0, location_index)].fillColor = colors.Color(28.0/255, 144.0/255, 153.0/255)
    drawing.add(bc)

    #Elements.append(drawing)

    if_elsewhere_para = Paragraph('<font face="times" size=12>CO<sub rise = -10 size' +
    ' = 8>2 </sub> emissions for the function if the computation had been performed elsewhere</font>', style = styles["Normal"])
    graph_data = [['Emission Comparison'], [if_elsewhere_para], [drawing]]
    graph_table = Table(graph_data, [6*inch], [.25*inch, .25*inch, .25*inch], hAlign="CENTER")
    graph_table.setStyle(TableStyle([('FONT', (0,0), (0,0), "Times-Bold"),
                                     ('FONT', (0,1),(0,1),"Times-Roman"),
                                     ('FONTSIZE', (0,0), (0,0), 13),
                                     ('FONTSIZE', (0,1), (0,1), 12),
                                     ('ALIGN', (0,0), (-1,-1), "CENTER")]))


    Elements.append(graph_table)



def generate(location, watt_averages, breakdown, kwh_and_emissions, func_info, comparison_values):
    # TODO: remove state_emission and just use location
    """ Generates pdf report

    Parameters:
        location (str): user's location
        watt_averages (list): list of baseline, total, process wattage, process duration
        breakdown (list): [% coal, % oil/petroleum, % natural gas, % low carbon]
        kwh_and_emissions (list): [kwh used, emission in kg CO2, state emission > 0 for US states]
        func_info (list): [user func name, user func args (0 or more)]

    """

    kwh, emission, state_emission = kwh_and_emissions
    baseline_average, process_average, difference_average, process_duration = watt_averages


    # Initializing document
    doc = SimpleDocTemplate("energy-usage-report.pdf",pagesize=landscape(letter), topMargin=.3*inch)

    title("Energy Usage Report")

    # Handling header with function name and arguments
    func_name, *func_args = func_info
    info_text = " for the function " + func_name
    if len(func_args) > 0:
        if len(func_args) == 1:
            info_text += " with the input " + str(func_args[0]) + "."
        else:
            info_text += " with the inputs "
            for arg in func_args:
                info_text += arg + ","
            info_text = info_text[len(info_text)-1] + "."
    else:
        info_text += "."

    subtitle("Energy usage and carbon emissions" + info_text, spaceBefore=True)

    # Energy Usage Readings and Energy Mix Data
    readings_data = [['Energy Usage Readings', ''],
                ['Average baseline wattage:', "{:.2f} watts".format(baseline_average)],
                ['Average total wattage:', "{:.2f} watts".format(process_average)],
                ['Average process wattage:', "{:.2f} watts".format(difference_average)],
                ['Process duration:', process_duration],
                ['','']] #hack for the alignment

    coal_para = Paragraph('<font face="times" size=12>996 kg CO<sub rise = -10 size = 8>2 </sub>/MWh</font>', style = styles["Normal"])
    oil_para = Paragraph('<font face="times" size=12>817 kg CO<sub rise = -10 size = 8>2 </sub>/MWh</font>', style = styles["Normal"])
    gas_para = Paragraph('<font face="times" size=12>744 kg CO<sub rise = -10 size = 8>2 </sub>/MWh</font>', style = styles["Normal"])
    low_para = Paragraph('<font face="times" size=12>0 kg CO<sub rise = -10 size = 8>2 </sub>/MWh</font>', style = styles["Normal"])
    if state_emission:
        coal, oil, natural_gas, low_carbon = breakdown
        mix_data = [['Energy Mix Data', ''],
                    ['Coal', "{:.2f}%".format(coal)],
                    ['Oil', "{:.2f}%".format(oil)],
                    ['Natural gas', "{:.2f}%".format(natural_gas)],
                    ['Low carbon', "{:.2f}%".format(low_carbon)]]
        equivs_data = [['Coal:', coal_para],
                       ['Oil:', oil_para],
                       ['Natural gas:', gas_para],
                       ['Low carbon:', low_para]]

    else:
        coal, petroleum, natural_gas, low_carbon = breakdown
        mix_data = [['Energy Mix Data', ''],
                    ['Coal',  "{:.2f}%".format(coal)],
                    ['Petroleum', "{:.2f}%".format(petroleum)],
                    ['Natural gas', "{:.2f}%".format(natural_gas)],
                    ['Low carbon', "{:.2f}%".format(low_carbon)]]
        equivs_data = [['Coal:', coal_para],
                       ['Petroleum:', oil_para],
                       ['Natural gas:', gas_para],
                       ['Low carbon:', low_para]]

    readings_and_mix_table(readings_data, mix_data, breakdown, state_emission, location)
    effective_emission = Paragraph('<font face="times" size=12>{:.2e} kg CO<sub rise = -10 size = 8>2 </sub></font>'.format(emission), style = styles["Normal"])
    # Total kWhs used and effective emissions
    kwh_and_emissions_data = [["Total kilowatt hours used:", "{:.2e} kWh".format(kwh)],
                              ["Effective emissions:", effective_emission]]

    kwh_and_emissions_table(kwh_and_emissions_data)

    # Equivalencies and CO2 emission equivalents
    per_house = Paragraph('<font face="times" size=12>% of CO<sub rise = -10 size = 8>2</sub> per US house/day:</font>'.format(emission), style = styles["Normal"])
    emissions_data = [
                 ['Miles driven:', "{:.2e} miles".format(convert.carbon_to_miles(emission))],
                 ['Min. of 32-in. LCD TV:', "{:.2e} minutes".format(convert.carbon_to_tv(emission))],
                 [per_house, \
                   "{:.2e}%".format(convert.carbon_to_home(emission))]]

    equivs_and_emission_equivs(equivs_data, emissions_data)


    comparison_graphs(comparison_values, location, emission)
    doc.build(Elements)
