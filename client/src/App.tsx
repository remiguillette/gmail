import { QueryClientProvider } from "@tanstack/react-query";
import { queryClient } from "./lib/queryClient";
import { Toaster } from "@/components/ui/toaster";

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div style={{ position: 'fixed', width: '100%', height: '100%', top: 0, left: 0 }}>
        <iframe 
          src="/index.html" 
          style={{ 
            width: '100%', 
            height: '100%', 
            border: 'none' 
          }}
          title="Split Panel Layout"
        />
      </div>
      <Toaster />
    </QueryClientProvider>
  );
}

export default App;