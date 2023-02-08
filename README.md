# network-anomalie-detection-
anamolies to detect suspecting activities
  we can detect suspecting DoS activities  based on uniformity of IP adresses:(needs knowledge of signature , cant detect new anomalies)
## Non signature based anomaly detection.
    principal components analysis PCA
    sketch-based
    signal analysis based
    its hard bcs :  many types of anomalies and methodes deal whith one kind
                    none is best 
                    the field needs evolution
## network anomalies can be caused by :
    chengees in link traffic volume 
    distributiin patterns of IP source or destinations
    flash crowds : large volume of traffic to  a single desstination
    routine table changes
    port scans : Probe to many destinations ports on a small number of destination addresses
    virus 
    worms : scanning by worms for vulanrable hosts , which is a special case if network scan
        network anomalies detection is a challenging probleme , because of the anomalies that  are hardly discernable
## PCA-based approaches:
    volume based detection : PCA
    Featre-based detection 
## sketch-based : 
    sliding window averaging
    exponential smoothing
    Box-jekins ARIME
    
        but the probleme here is scallabality , a large number for each flow defined , the solution to this scalability is to use data stream computation, we use a probalitic summary methodes that uses  random projections , its called the sketch . we use this methodes because its space efficient and provide reconstruction accuracy guarantees , it needs constant update cist
first we begin whith PCA-based approaches:
 we are gonna specialise in detecting small volume, correlated anomalies instead of large volme anomalises that other methode specialaise in.
 ths methode is gonna separate the trafic into normal and abnormal ,which achieves three objectives:
       detect anomalies
       identifying the underlying origine-destination flows that are the sources of the anomalies
        estimating the amount of traffic involved
# PCA :
is a coordinate transformation that maps a set of data points onto new axes called principale axes .the firs principale componet point in the the direction of maximum variance . the second principae direction is the maximum variance remaining in the residue data after removing variance already accounted for by the first principale components.thus it can be used for dimension reduction.

for this methodes we need an understanding in mathematical terms such as covariance and variance ,matrices manipulation and estimations .
