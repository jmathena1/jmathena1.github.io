/**
 * Live Reload Client
 * 
 * Connects to the dev server via WebSocket and automatically reloads the page
 * when the site is rebuilt, or displays errors in the console.
 */

(function() {
  // Only enable on localhost (dev environment)
  if (window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1') {
    return;
  }

  const WS_URL = `ws://${window.location.host}/ws`;
  const MAX_RETRIES = 10;
  const INITIAL_RETRY_DELAY = 1000; // 1 second
  const MAX_RETRY_DELAY = 30000; // 30 seconds
  
  let ws = null;
  let retryCount = 0;
  let retryDelay = INITIAL_RETRY_DELAY;
  let reconnectTimeout = null;

  function log(message) {
    console.log(`[Live Reload] ${message}`);
  }

  function error(message) {
    console.error(`[Live Reload] ${message}`);
  }

  function connect() {
    try {
      log(`Connecting to dev server... (attempt ${retryCount + 1}/${MAX_RETRIES})`);
      ws = new WebSocket(WS_URL);

      ws.onopen = function() {
        log('Connected to dev server ✓');
        retryCount = 0;
        retryDelay = INITIAL_RETRY_DELAY;
      };

      ws.onmessage = function(event) {
        try {
          const message = JSON.parse(event.data);
          
          if (message.status === 'rebuild_complete') {
            log('Build complete, reloading page...');
            // Delay reload slightly to ensure assets are ready
            setTimeout(() => {
              window.location.reload();
            }, 100);
          } 
          else if (message.status === 'rebuild_failed') {
            error(message.error);
          }
          else if (message.status === 'rebuild_timeout') {
            error(message.error);
          }
        } catch (e) {
          error(`Failed to parse message: ${e.message}`);
        }
      };

      ws.onerror = function(event) {
        error(`WebSocket error: ${event.type}`);
      };

      ws.onclose = function() {
        log('Disconnected from dev server');
        scheduleReconnect();
      };

    } catch (e) {
      error(`Connection failed: ${e.message}`);
      scheduleReconnect();
    }
  }

  function scheduleReconnect() {
    if (retryCount >= MAX_RETRIES) {
      error(`Failed to connect after ${MAX_RETRIES} attempts. Giving up.`);
      return;
    }

    retryCount++;
    
    // Exponential backoff with jitter
    const jitter = Math.random() * 0.1 * retryDelay;
    const nextDelay = Math.min(retryDelay * 2, MAX_RETRY_DELAY) + jitter;
    
    log(`Retrying in ${Math.round(retryDelay / 100) / 10} seconds...`);
    
    reconnectTimeout = setTimeout(() => {
      connect();
      retryDelay = nextDelay;
    }, retryDelay);
  }

  // Clean up on page unload
  window.addEventListener('beforeunload', function() {
    if (reconnectTimeout) {
      clearTimeout(reconnectTimeout);
    }
    if (ws) {
      ws.close();
    }
  });

  // Initial connection
  log('Initializing live reload...');
  connect();
})();
