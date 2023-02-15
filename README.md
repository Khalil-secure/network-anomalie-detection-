# network-anomalie-detection
  we can detect suspecting DoS activities  based on uniformity of IP adresses:(needs to be known  signature , cant detect new anomalies) as it is now i am studying the classical of detect anomalies in the field of cybersecurity ,then i am gonna get interested in implementing Ai in detecting virus and worms that are not registered but still has effect that can be identified .
# Non signature based anomaly detection.
 principal components analysis PCA
    sketch-based
    signal analysis based
    this type of anomalies detection is complicated because : a signature based needs data on the exact same virus for it to detect it so the hacker just need another code of a virus for him to pass by the firewall .
# network anomalies can be caused by :
changes in link traffic volume 
distributiin patterns of IP source or destinations
flash crowds : large volume of traffic to  a single desstination
routine table changes
port scans : Probe to many destinations ports on a small number of destination addresses
virus 
worms : scanning by worms for vulanrable hosts , which is a special case if network scan
        network anomalies detection is a challenging probleme , because of the anomalies that are hard to discerne
 PCA-based approaches:
    volume based detection : PCA
    Featre-based detection 
 sketch-based : 
    sliding window averaging
    exponential smoothing
    Box-jekins ARIME
# scallabality
 but the probleme here is a large nomber of data needs to be analysed , the solution to this scalability is to use data stream computation, we use a probalitic summary methodes that uses  random projections , its called the sketch . we use this methodes because its space efficient and provide reconstruction accuracy guarantees , it needs constant update cist
first we begin whith PCA-based approaches:
 we are gonna focus in detecting small volume, correlated anomalies instead of large volme anomalises that other methode specialise in.
 ths methode is gonna separate the trafic into normal and abnormal ,which achieves three objectives:
       detect anomalies
       identifying the underlying origine-destination flows that are the sources of the anomalies
        estimating the amount of traffic involved
# PCA :
is a coordinate transformation that maps a set of data points onto new axis called principale axes .the first principale componet point in the the direction of maximum variance . the second principale direction is the maximum variance remaining in the residue data after removing variance already accounted for by the first principale components.thus it can be used for dimension reduction.

for this methodes we need an understanding in mathematical terms such as covariance and variance ,matrices manipulation and estimations .
the code that i am presenting is gonna use the PCA fonction that already exist in the library
and another code that gonna detail mathematically the PCA function .

# my next project is gonna be using AI in detecting anomalies in the systeme
    

    
