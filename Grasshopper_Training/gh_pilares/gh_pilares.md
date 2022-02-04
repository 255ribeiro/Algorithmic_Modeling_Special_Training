# Grasshopper Pilar sequence

_______________


## Starting a definition

[Pilar_sequence: base file](./Grasshopper_introdução.gh)

To start a setting on **Grashopper** click on the componete **Point** of the tab **Params** in the **Geometry** panel. Click the work screen (*canvas*) to position the componete in the code editor.

![Componente Point](./pointComp.jpg)

With the componete **Point** on canvas, right-click on the component and select the **Set One Point** option.

![Set One Point](./setOnepoint.jpg)

The **Set One Point** option toggles to the interface of **Rhino**, allowing the selection of a point by coordinates, by a point drawn on the interface of **Rhino** or a point on a curve. If the *Coordinates* option is not appearing on the command line, click on the text **Type** and select the coordinates option

![Set Point Type](./setPointType.png)

With the coordinates option selected, the point can be selected by clicking on the screen or typing the corrdenadas.

![Set Coord](./setPointCoord.png)

Enter the coordeandas 0,0,1 and press **enter** to return to the interface of **Grasshopper**.

To move the point in a specific direction and distance, click the **Trasnform** tab on the **Euclidean* panel, select the **Move** component.

![move](./MoveComp.png)

Drag the output to the left of the **Point** component and concect the **Geometry** entry of the **Move** component. With this the point will be moved in the distance and *default* direction of the component (10 units in the direction of the Z axis).

![Move Geometry](./MoveConect.png)

![Move Geometry 2](./move2.png)

### Setting Distance Direction

To set a direction, in the **Vector** tab in the **Vector** panel, select the **Unit Z** component. connect the component output to the component **Motion** input **Move**.

![Unit z](./unitZ.png)

The **Unit Z** component is a unit vector in the z direction. To set the distance, in the tab **Params**, in the panel **Input** select the option **Slider**.

![Slider 1](./slider1.png)

Com um clique duplo na parte esquerda do **Slider**, altere o valor da opção **MAx** para 100 e clique em **Ok**. Conecte a saída do **Slider** na entrada do componente **Unit Z**.

![Edit Slider](./editSlider.png)

### Creating a line conecting 2 points

![line](./line1.png)

Double-click the left side of the **Slider**, change the value of the **MAx** option to 100 and click **Ok**. Connect the **Slider** output to the component input **Unit Z**.

![line 2](./line2.png)

### Creating a Column (pipe) From a Line

![pipe1](./pipe1.png)

On the **Surface** tab on the **Freeform** panel, select the **Pipe** component. Check the output of the **Line** component at the **Curve** input of the **Pipe** component. Connect a **Slider** to the **Radius** input of the **Pipe** component. In the **Cap** entry of the **Pipe** component, right-click and select the **Flat** option.

![pipe2](./pipe2.png)

### Creating columns along a curve

In **Rhinoceros** draw a line segment or a curve.

In **params** tab, in **Geometry** panel, select the **Curve** component.

![curve1](./curve1.png)

Right-click on the component and select the curve on **Rhinoceros** by clicking on the curve.

![curve2](./curve2.png)

Na aba **Curve**, no painel **Division** selecione o componente **Divide Curve**.

![Divide Curve1](./divideCurve1.png)

In the **Curve** tab, in the **Division** panel select the **Divide Curve** component.

![Divide Curve 2](./divideCurve2.png)

In the **Params**tab, in the **Input* panel select the **Slider** option.

![slider int 1](./sliderInt1.png)

Double-clicking on the left side of **Slider**, change the value of the **R** option to **N** and the **Max** option to 100 and click **Ok**.

![slider int 2]./(sliderInt2.jpg)

Connect the **Slider** output with the **Count** input of the **Divide Curve** component.

![slider int 3](./sliderInt3.png)

Connect the **Points** output of the **Divide Curve** component to the input of the **Point** component.

![points point](./Points_Point.png)

Final algorithm

![exemplo01](./exemplo01.png)

[Download](./seq_pilares_final.gh) Final example file.

## Other Examples:

[Elementos tubulares uma Curva](./ELEMENTOS_TUBULARES_UMA_CURVA.gh)

[Elementos tubulares duas Curvas](./ELEMENTOS_TUBULARES_DUAS_CURVAS.gh)

[Exemplo Janelas](./exemplo_janela.gh)

[Guarda Corpo](./GUARDA-CORPO.gh)

[Exemplo Mies](./Exemplo_Mies_rhino7.gh)

[Exemplo Python](https://github.com/jonasbarbosa/trabalhofinalLPACAF)
