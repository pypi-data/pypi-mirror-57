
.. code:: ipython3

    from ImageDiffOps import ImageDiffOpsmageDiffOps

.. code:: ipython3

    imDfOps = ImageDiffOps("C:\\Users\\Desktop\\nik\\Test\\marked\\1.png","C:\\Users\\Desktop\\nik\\Test\\unmarked\\1.jpg")

.. code:: ipython3

    imgs,cord = imDfOps.detectDiffROI()

.. code:: ipython3

    imDfOps.SimilarityScore()




.. parsed-literal::

    0.9762137787644005



.. code:: ipython3

    imDfOps.SimilarityScore()

.. code:: ipython3

    import matplotlib.pyplot as plt
    # setup the figure
    
    plt.title("extracted image parts where change has happend")
    for img in imgs:
        
        
        plt.imshow(img, cmap=plt.cm.gray)
        plt.show()  



.. image:: output_5_0.png



.. image:: output_5_1.png



.. image:: output_5_2.png



.. image:: output_5_3.png



.. image:: output_5_4.png



.. image:: output_5_5.png



.. image:: output_5_6.png


