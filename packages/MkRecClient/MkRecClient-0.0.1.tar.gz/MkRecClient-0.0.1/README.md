<html>

<head>
    <link rel="stylesheet" type="text/css" href="https://mknxgn.pro/styles/main.css">
    <link rel="stylesheet" type="text/css" href="https://mkrec.mknxgn.pro/rainbow.css">
    <script src="https://mkrec.mknxgn.pro/rainbow.js"></script>
    <style>
        @font-face {
            font-family: MkFont;
            src: url(https://mkrec.mknxgn.pro/MkFont.ttf);
        }

        .title {
            font-family: MkFont;
            font-size: xx-large;
            padding: 10px;
            text-align: center;
        }
    </style>
</head>

<body>
    <div style="text-align: center;">
        <div class="title" style="font-size: 60px;">
            MK Rec
        </div>
        <div style="font-style: italic;">
            Open Image Recognition - Client
        </div>
    </div>
    <div style="padding: 20px 50px">
        Created By Mark @ MkNxGn<br><br>
        <pre><code data-language="python">pip install MkRecClient</code></pre>
        Use this module to interact with MkRec on a programmatic level with python! Build an API for your uses to use
        your services with MkRec and build awesome applications.
        <br><br><br>
        Register your client with the server for maximum security!
        <pre><code data-language="python">#Register the client
usr = input("My Username: ")
MkRecClient.Register_Client(usr)</code></pre>
        <br>

        Get a list of active machines
        <pre><code data-language="python">#Get Machines
MkRecClient.Register_Client()
print(MkRecClient.get_machines())</code></pre>
<br>

        Get Machine Trained Titles, What the machines knows
        <pre><code data-language="python">#Get Machine Trained Titles, What the machines knows
MkRecClient.Register_Client()
Machines = MkRecClient.get_machines()
print(Machines['Animals'].titles)</code></pre><br>
    
        Get Machine Training Stats
    <pre><code data-language="python">#Get Machine Training Data
MkRecClient.Register_Client()
Machines = MkRecClient.get_machines()
print(Machines['Animals'].train_acc) #Machine accuracy
#  OR
print(Machines['Animals'].training) #All stats</code></pre><br>
Get the value of points attached to your account
<pre><code data-language="python">#Get the value of points attached to your account
MkRecClient.Register_Client()
print(MkRecClient.get_points())</code></pre><br>
And Finally, what we've all been waiting for, how to send an image to the machine!
<pre><code data-language="python">#Send an Image to get results!
result = MkRecClient.PredictImage(MkRecClient.prep_img("img.png"), "Animals")
result.result #the best result
result.all_results #all results
result.remaing_points #how many points you have now
result.possible_titles #all possible titles of the machine
#if the result wasn't correct, and you had heap=True
result.correct('correct class')
</code></pre>
</div>
</body>

</html>