--- src/yaws_server.erl.old	2009-08-01 18:57:30.097138117 -0400
+++ src/yaws_server.erl	2009-08-01 19:49:38.053920838 -0400
@@ -2091,9 +2091,16 @@
                 {_Prefix,URL,Mode})  when is_record(URL,url) ->
     ?Debug("in redir 302 ",[]),
     H = get(outh),
-    DecPath = safe_decode_path(Req#http_request.path),
-    {P, Q} = yaws:split_at(DecPath, $?),
     LocPath = yaws_api:format_partial_url(URL, get(sc)),
+    [_Scheme, _Host, _Port, Path, _Query] = LocPath,
+    Last = lists:last(Path),
+    DecPath = case safe_decode_path(Req#http_request.path) of
+                  [$/|Rel] when Last == $/ ->
+                      Rel;
+                  Abs ->
+                      Abs
+              end,
+    {P, Q} = yaws:split_at(DecPath, $?),
     Loc = if
               Mode == append, Q == [] ->
                   ["Location: ", LocPath, P, "\r\n"];
