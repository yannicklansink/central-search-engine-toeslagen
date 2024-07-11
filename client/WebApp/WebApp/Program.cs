using WebApp.Client.Pages;
using WebApp.Components;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// for enabling the
//  - Interactive Server,
//  - Interactive WebAssembly,
//  - Interactive Auto
// render modes:
builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents()
    .AddInteractiveWebAssemblyComponents();

// Load configuration from appsettings.json and appsettings.{Environment}.json
var configuration = builder.Configuration;

// Register the HttpClient
builder.Services.AddHttpClient("RAGClient", client =>
{
    client.BaseAddress = new Uri(configuration["HttpClientSettings:BaseUrl"]);
});

builder.Services.AddSingleton<MyRAGService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseWebAssemblyDebugging();
}
else
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();
app.UseAntiforgery();

// configure services
// for enabling the
//  - Interactive Server,
//  - Interactive WebAssembly,
//  - Interactive Auto
// render modes:
app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode()
    .AddInteractiveWebAssemblyRenderMode()
    .AddAdditionalAssemblies(typeof(Counter).Assembly);


app.Run();
