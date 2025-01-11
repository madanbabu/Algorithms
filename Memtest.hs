import System.Mem
import Control.Monad

testMemory :: Int -> IO ()
testMemory size = do
    let data = listArray (1, size) (repeat ())
    memBefore <- getForeignAllocations
    deepseq data ()
    memAfter <- getForeignAllocations
    let memUsed = memAfter - memBefore
    putStrLn $ "Allocated " ++ show size ++ " elements, used " ++ show memUsed ++ " bytes"

main :: IO ()
main = do
    putStrLn "Starting memory test..."
    mapM_ (testMemory . (2 ^)) [1..24]
    putStrLn "Memory test completed."
