topic = 'Data Structure and Algorithm'
topic2 = 'Object Oriented Programming'
topic3 = 'Computer Network'
topic4 = 'SQL Database'
topic5 = 'Operating System'
topic6 = 'Machine Learning'
topic7 = 'Natural Language Processing'
topic8 = 'Computer Vision'


domainDSA = [
    'distance problem', 'scheduling', 'binary search tree', 'balance binary search tree',
    'hasing', 'chaining','hash function', 'table doubling', 'karp-rabin', 'sorting with heaps',
    'linear bounds', 'linear time sorting', 'stable sorting', 'radix sort', 'graph search', 'numerics 1', 
    'Depth First Search', 'Breadth First Search', 'topological sort', 'shortest path', 'Dijkstra', 
    'Bellman-Ford','speed-up Dijkstra', 'dynamic programming - memoization, fibonacci, crazy eights, guessing', 
    'dynamic programming - text justification, parenthesization, knapsack, pseudopolynominal time, tetris training',
    'longest common subsequence', 'parent pointers', 'dynamic programming - piano fingering, structural DP(trees), vertex cover,dominating set, beyond',
    'numerics 2'
]
domainOOP = [
    'OBJECT-ORIENTED PARADIGM', 'JAVA BACKGROUND', 'Java syntax basics',
    'Identifiers and keywords', 'Data types and Literals', 'Comment line arguments',
    'Operators', 'Expression', 'Statement', 'Abstraction', 'class', 'attributes and operations',
    'message passing', 'visibility scope', 'package', 'class declaration', 'variables declaration',
    'method declaration', 'data initialization and constructor', 'object declaration and initialization', 
    'object usage', 'Encapsulation - visibility scope', 'Encapsulation - data hiding', 'Overloading - principles',
    'Overloading - constructor overloading', 'Aggregation - principles', 'Aggregation - order of initialization', 
    'Class usage', 'Inheritance - principles', 'Inheritance hierarchy', 'Inheritance - subclass definition', 'Inheritance - order of initialization',
    'Method overriding', 'Single inheritance and multiple inheritance', 'Abstract class and Abstract method', 'Interface and implementation',
    'Polymorphism', 'Downcasting and upcasting', 'Overloading', 'Method call binding','Generic programming', 'String and StringBuffer',
    'Collections Interface', 'ArrayList class', 'HashSet class', 'HashMap class', 'Iterator and Comparator interface', 
    'Exception and exception handling','Exception classes hierarchy', 'try/catch/finally blocks', 'Throwing exceptions', 'Print a stack trace message',
    'Making custom exceptions', 'Basic input and output', 'File manipulation', 'Input and output with Scanner and printf',
    'Programming GUI with AWT', 'AWT Event-Handling', 'AWT Menu', 'Programming GUI with Swing', 'SOLID principles', 
    'Single-Responsibility Principle', 'Single-Responsibility Principle', 'Liskov Substitution Principle', 'Interface Segregation Principle', 
    'Dependency Inversion Principle', 'Patterns', 'Creational Patterns - Factory Method Pattern',
    'Structural Patterns - Adapter Pattern', 'Behavioral Patterns - Observer Pattern'
]
domainNLP = []
domainAdvancedNLP = [
    'parsing problem', 'context free grammars', 'PCFG', 'weakness of PCFG',
    'language modeling problem', 'smoothed n-grams estimate',
    'PCFG', 'context free rules', 'parse trees', 'EM algortihm' ,'Hidden Markov Model with brute force', 'Hidden Markov Model with dynamic programming',
    'lexicon-based similarity using word-net relations' 'lexicon-based similarity using path-based similarity', 
    'corpus-based similarity using vector space model', 'corpus-based similarity using similairty measures', 'corpus-based similarity using hierarchical clustering',
    'lexical semantics using vector-based similarity', 'lexical semantics using probabilistic similarity','lexical semantics using k-Mean algorithm',
    'log-linear model', 'iterative scaling', 'gradient ascent', 'conjudate gradient ascent', 'maximum entropy of log-linear model', 'smoothing Methods Using Gaussian Prior', 'feature Selection Method', 
    'Hidden Markov Model Taggers', 'log-linear Taggers', 'log-linear Models For Parsing', 'language Acquisition Problem with vocabulary Induction', 
    'language Acquisition Problem with Hidden Markov Model Topology Induction', 'language Acquisition Problem with PCFG Induction', 
    'discourse Model with cohesion-Based', 'discourse Model with content-Based', 'discourse Model with rhetorical', 
    'segmentation with agreement and Evaluation', 'segmentation with hearsts Segmentation Algorithm', 
    'text Segmentation', 'local Coherence', 'coreference Resolution',
    'statistical Machine Translation', 'evaluation Machine Translation System', 'sentence Alignment Problem', 'IBM Model 1',
    'structure IBM', 'EM Tranining', 'Decoding', 'phrase-BasedModel', 'syntax-Based Model 1', 'syntax-Based Model 2',
    'graph-Based Algorithm with hubs And Authorities', 'graph-Based Algorithm with min-Cut',
    'application in information Retrieval', 'application in summarization', 'application in generation',
    'word Sense Disambiguation', 'global Linear Mode', 'reranking Problem', 'perception Algorithm',
    'text Summarization', 'log-Linear Model For Parameters Estimation', 'global and Local Features', 
    'Hidden Markov Model For DA Labeling', 'architecture Of Dialogue Systems', 'statistical Model For NLU', 
    'statistical NLU', 'Reinforcement Learning For Dialogue', 'planning-Based Agent System'
]
domainCV = [
    'Image Formatio, Perspective Projection, Time Derivative, Motion Field', 
    'Time to Contact, Focus of Expansion, Direct Motion Vision Methods, Noise Gain', 
    'Fixed Optical Flow, Optical Mouse, Constant Brightness Assumption, Closed Form Solution',
    'TTC and FOR Montivision Demos, Vanishing Point, Use of VPs in Camera Calibration',
    'Photometric Stereo, Noise Gain, Error Amplification, Eigenvalues and Eigenvectors Review',
    'Gradient Space, Reflectance Map, Image Irradiance Equation, Gnomonic Projection',
    'Shape from Shading, Special Cases, Lunar Surface, Scanning Electron Microscope, Greens Theorem in Photometric Stereo',
    'Shape from Shading, General Case - From First Order Nonlinear PDE to Five ODEs',
    'Characteristic Strip Expansion, Shape from Shading, Iterative Solutions',
    'Edge Detection, Subpixel Position, CORDIC, Line Detection',
    'Blob analysis, Binary Image Processing, Use of Greens Theorem, Derivative and Integral as Convolutions',
    'Object detection, Recognition and Pose Determination, PatQuick',
    'Inspection in PatQuick, Hough Transform, Homography, Position Determination, Multi-Scale',
    'Alignment, recognition in PatMAx, distance field, filtering and sub-sampling',
    'Fast Convolution, Low Pass Filter Approximations, Integral Images',
    'Photogrammetry, Orientation, Axes of Inertia, Symmetry, Absolute, Relative, Interior, and Exterior Orientation',
    'Rotation and How to Represent it, Unit Quaternions, the Space of Rotations',
    'Absolute Orientation in Closed Form, Outliers and Robustness, RANSAC',
    'Space of Rotations, Regular Tessellations, Critical Surfaces in Motion Vision and Binocular Stereo',
    'Relative Orientation, Binocular Stereo, Structure from Motion, Quadrics, Camera Calibration, Reprojection',
    'Exterior Orientation, Recovering Position and Orientation,Bundle Adjustment, Object Shape',
    'Gaussian Image and Extended Gaussian Image, Solids of Revolution, Direction Histograms, Regular Polyhedra'
]