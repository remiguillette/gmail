import { Route, Switch } from "wouter";
import { QueryClientProvider } from "@tanstack/react-query";
import { queryClient } from "./lib/queryClient";
import { Toaster } from "@/components/ui/toaster";
import NotFound from "@/pages/not-found";

function StaticPage() {
  return (
    <div style={{ position: 'fixed', width: '100%', height: '100%', top: 0, left: 0 }}>
      <iframe 
        src="/index.html" 
        style={{ 
          width: '100%', 
          height: '100%', 
          border: 'none' 
        }}
        title="Static Split Panel Layout"
      />
    </div>
  );
}

function Router() {
  return (
    <Switch>
      <Route path="/" component={StaticPage} />
      <Route component={NotFound} />
    </Switch>
  );
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router />
      <Toaster />
    </QueryClientProvider>
  );
}

export default App;
