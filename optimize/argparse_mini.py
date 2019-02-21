from scipy.optimize import minimize
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--a",type=int,default=1,help="please input the argument a")
parser.add_argument("--b",type=int,default=2,help="please input the argument b")
parser.add_argument("--c",type=int,default=3,help="please input the argument c")
parser.add_argument("--init",type=float,default=2)
def fun(args):
    y=lambda x:(x-args.a)*(x-args.b)*(x-args.c)
    return y
if __name__=="__main__":
    args=parser.parse_args()
    res=minimize(fun(args),args.init)
    print(res.fun)
    print(res.success)
    print(res.x)
