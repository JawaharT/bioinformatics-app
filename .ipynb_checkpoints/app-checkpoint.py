import streamlit as st
from Bio.Seq import Seq
from Bio import SeqIO
from collections import Counter,OrderedDict

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

def main():
    """Simple Bioinformatics App. """

    st.title("Simple Bioinformatics App")
    menu = ["Intro", "DNA", "Dot Plot", "About"]
    choices = st.sidebar.selectbox("Select Activity", menu)

    if choices == "Intro":
        st.subheader("Intro to Bioinformatics")

    elif choices == "DNA":
        st.subheader("DNA Sequence Analysis")

        seq_file = st.file_uploader("FASTA File Upload", type=["fasta","fa"])

        if seq_file is not None:
            record = SeqIO.read(seq_file,"fasta")

            full_seq = record.seq
            file_details = st.radio("Details", ("Description", "Sequence"))

            if file_details == "Description":
                st.write(record.description)
            elif file_details == "Sequence":
                st.write(full_seq)

            #Nucleotide occurances
            st.subheader("Nucleotide Frequency")
            full_seq_freq = OrderedDict(Counter(full_seq))
            st.write(full_seq_freq)

            bar1_colour = st.beta_color_picker("Pick Colour for Bar 1")
            bar2_colour = st.beta_color_picker("Pick Colour for Bar 2")
            bar3_colour = st.beta_color_picker("Pick Colour for Bar 3")
            bar4_colour = st.beta_color_picker("Pick Colour for Bar 4")
            
            if st.button("Plot Freq"):
                barlist = plt.bar(full_seq_freq.keys(), full_seq_freq.values())
                barlist[0].set_color(bar1_colour)
                barlist[1].set_color(bar2_colour)
                barlist[2].set_color(bar3_colour)
                barlist[3].set_color(bar4_colour)
                st.pyplot()

            st.subheader("DNA Composition")
            gc_count = full_seq.gc_content()
            
            
    
    elif choices == "Dot Plot":
        st.subheader("Dot Plot Generator")

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
