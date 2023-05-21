import streamlit as st

class UI:
    def __init__(self):
        st.set_page_config(layout="wide")
        self.title = st.container()
        self.seach_tab = st.container()
        self.id = int()
        self.data = {
            "Office Address": "B-164-165-166-185-186-187, BSCIC I/E, SHASONGAON FATULLAH, NARAYANGANJ, DHAKA BANGLADESH",
            "Factory Address": "B-164-165-166-185-186-187, BSCIC I/E, SHASONGAON FATULLAH, NARAYANGANJ, DHAKA BANGLADESH",
            "Employees": "550",
            "Production Capacity": "375000",
            "Company Name": "M B KNIT FASHION LTD.",
            "BKMEA Membership Number": "1",
            "Representative Name": "MR. MOHAMMAD HATEM",
            "Representative Designation": "MANAGING DIRECTOR",
            "Representative Mobile": "01711533228, 01552462030",
            "Representative Email": "hatem.mbknit@gmail.com",
            "Production Machines": "360",
        }
        self.display_info_header = st.container()
        self.display_info_body = st.container()
        self.ui()

    def ui(self):
        with self.title:
            self.title.title("Company information")
            title_alignment = """
                        <style>
                        #company-information {
                          text-align: center
                        }
                        </style>
                        """
            self.title.markdown(title_alignment, unsafe_allow_html=True)

        with self.seach_tab:
            self.id = self.seach_tab.text_input(label='Company ID', value='Company ID', label_visibility='collapsed')

        with self.display_info_header:
            col1, col2, col3 = self.display_info_header.columns(3)
            col2.subheader('Primary Informations')
            text_alignment = """
                                    <style>
                                    #primary-informations {
                                      text-align: center
                                    }
                                    </style>
                                    """
            col2.markdown(text_alignment, unsafe_allow_html=True)

        with self.display_info_body:
            self.display_info_body.table(self.data)