# Script to create Diagram for TriNetX Hypercapnia venn diagram

from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt

def venn_diagram():
    venn3(subsets=(250179, 72758, 56125, 59945, 39518, 7987, 15413), set_labels=('PaCO2 >= 45 mmHg\non ABG ', 'ICD-10 code of\nhypercapnic\nrespiratory failure', 'Procedure code\nfor NIV'), alpha=0.7);
    #plt.title("Overlap of Differing Definitions of Hypercapnic Respiratory Failure")
    plt.savefig('Hypercapnia Venn Diagram.png', transparent=True)
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    venn_diagram()
